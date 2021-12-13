
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

def computeStats(filename, show_output = True):
    with open(filename) as file:
        pr=pd.read_csv(file,'\t')#read csv into dataframe
    
    count=0    
    basescontig=0
    basegap=0
    if show_output:
        for i in range(len(pr['c_end'])):
            if pr['c_end'][i]=='yes':
                count+=1
                basegap+=(pr['s_end'][i]-pr['s_start'][i])  
            else:
                basescontig+=(pr['s_end'][i]-pr['s_start'][i]) 
        print('the file contains ',len(pr['ScaffID']),' enrties')
        print('... ',len(pr['ScaffID'].unique()),' scaffolds')
        print('... ',len(pr['contig'].unique()),' contigs (tot_size: ',basescontig,' bases)')
                
        print('... and',count,' gaps (tot_size: ',basegap,' bases)')
    return pr    
def printSequence(scaffInfo, scafID, sequenceFile):
    return 0

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
