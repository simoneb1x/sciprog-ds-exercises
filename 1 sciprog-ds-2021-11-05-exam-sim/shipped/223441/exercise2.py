
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):

    # opening file and saving data into a dictionary
    dd = {}
    with open(filename,"r") as f:
        for line in f:
            line = line[:-1].split("\t") 
            if line[0] == "ScaffID":
                keys = line
                for k in keys:
                    dd[k] = []
            else:
                for i, k in enumerate(keys):
                    dd[k].append(line[i])
    

    # creating dataframe from dd
    df = pd.DataFrame(dd)

    if show_output:
        tot_e = len(df)
        tot_s = len(df["ScaffID"].unique())
        tot_c = len(df["contig"].unique())
        tot_g = len(df[df["type"]=="N"])
        gc = df.groupby("type")[["c_end","c_start","contig"]]
        c_df = gc.get_group("W")
        c_size = sum(c_df["c_end"].astype(int)- c_df["c_start"].astype(int))
        g_df = gc.get_group("N")
        g_size = g_df["contig"].astype(int).sum() 
        
        print(f"""The file contains {tot_e} entries
... {tot_s} scaffolds
... {tot_c} contigs (tot. size: {c_size:,} bases)
... and {tot_g} gaps (tot. size: {g_size:,} bases)""")

    return df

    
                

def printSequence(scaffInfo, scafID, sequenceFile):
    raise Exception("TODO IMPLEMENT ME !")

fn = "data_reduced.agp"
scaffDF = computeStats(fn)
scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")
