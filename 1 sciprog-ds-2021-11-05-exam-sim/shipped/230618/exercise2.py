
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    data=pd.read_csv(filename, sep="\t")
    if not show_output:
        return data
    entries=len(data)
    print("The file contains {} entries".format(entries))
    scaffold=len(data.groupby("ScaffID"))
    print("... {} scaffolds".format(scaffold))
    contigs=len(data[data["contig"]!="500"])
    gaps=len(data[data["contig"]=="500"])
    cont=data[data["contig"]!="500"]
    sizec=cont["c_end"].astype(int)-cont["c_start"].astype(int)
    totsizec=sizec.sum()
    print("... {} contigs (tot.size: {} bases)".format(contigs,totsizec))
    cont=data[data["contig"]=="500"]
    sizeg=cont["c_end"].astype(int)-cont["c_start"].astype(int)
    totsizeg=sizeg.sum()
    print("... and {} gaps (tot.size: {} bases)".format(gaps,totsizeg))
    return

def printSequence(scaffInfo, scafID, sequenceFile):
    return

fn = "data_reduced.agp"
scaffDF = computeStats(fn)
"""scaffDF = computeStats("small.agp", show_output = False)
printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")"""
