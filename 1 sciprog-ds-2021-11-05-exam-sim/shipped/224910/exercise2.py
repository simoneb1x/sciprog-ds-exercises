
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    """gets the filename of a .agp file as explained above, stores its content in a suitable data structure
    of your choice (hint: pandas might help here). If show_output is False the function only returns the datastructure"""
    df = pd.read_csv(f"{filename}", sep = "\t")
    print(df)
    return 0

def printSequence(scaffInfo, scafID, sequenceFile):
    raise Exception("TODO IMPLEMENT ME !")

fn = "data_reduced.agp"
scaffDF = computeStats(fn)
#print(scaffDF.head())
quit()
scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")
