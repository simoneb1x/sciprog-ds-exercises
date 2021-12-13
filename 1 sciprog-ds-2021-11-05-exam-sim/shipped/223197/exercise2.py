
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    df_agp=pd.read_csv(filename,sep='\t')
    if show_output:
        print('Total number of entries: ',df_agp.shape[0])
        print('Total number of scaffolds: ',df_agp['ScaffID'].unique().shape[0])
        print('Total number of contigs: ',df_agp['contig'].unique().shape[0])
        print('Total contig size: ','Total gaps: ')
        #group=df_agp.groupby('ScaffID')
        #aggdf=group.aggregate(pd.DataFrame.shape[0])
        #aggdf.plot(kind='box')
        #plt.show()
    return df_agp
    #raise Exception("TODO IMPLEMENT ME !")

def printSequence(scaffInfo, scafID, sequenceFile):
    if scafID in scaffInfo['ScaffID']:
        for rec in SeqIO.parse(sequenceFile,'fasta'):
            print(rec)
    #raise Exception("TODO IMPLEMENT ME !")

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
