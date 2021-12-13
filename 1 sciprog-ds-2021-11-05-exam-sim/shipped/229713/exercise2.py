
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    
    data = pd.read_csv(filename, sep ="\t", header = 0)
    
    if show_output:
        
        gaps_len = [el["c_stop"] for el in data[data["type"]=="W"]]

        print(
'''The file contains {num_entries} entries
... {num_scaff} scaffolds
... {num_contigs} contigs (tot. size: {count_bases} bases)
... and {num_gaps} gaps (tot. size: {count_gaps} bases)'''.format(
            num_entries = data.shape[0],
            num_scaff = len(data["ScaffID"].unique()),
            num_contigs = len(data[data["type"]=="W"]["contig"].unique()),
            count_bases = gaps_len,
            num_gaps = len(data[data["type"]=="N"]["contig"]),
            count_gaps = data[data["type"]=="N"]["contig"].astype(int).sum()
            )
        )

    return(data)


def printSequence(scaffInfo, scafID, sequenceFile):
    raise Exception("TODO IMPLEMENT ME !")

fn = "data_reduced.agp"
scaffDF = computeStats(fn)

'''
scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")
'''
