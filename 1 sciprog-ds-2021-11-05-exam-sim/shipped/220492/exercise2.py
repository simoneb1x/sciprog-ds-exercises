
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    DF=pd.read_csv(filename,sep="\t")
    print(type(DF))
    return 1
    #raise Exception("TODO IMPLEMENT ME !")

def printSequence(scaffInfo, scafID, sequenceFile):
    return 1
    #raise Exception("TODO IMPLEMENT ME !")

fn = "data_reduced.agp"
scaffDF = computeStats(fn)
scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
#print("")
#printSequence(scaffDF,"my_scaff2","small_seq.fasta")
#print("")
#printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
#print("")
#printSequence(scaffDF,"scaffold3","small_seq.fasta")
