
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    df=pd.read_csv(f"{filename}", sep="\t")
    #if show_output == False
    print(df)

def printSequence(scaffInfo, scafID, sequenceFile):
    raise Exception("TODO IMPLEMENT ME !")

fn = "data_reduced.agp"
scaffDF = computeStats(fn)
quit()
scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")
