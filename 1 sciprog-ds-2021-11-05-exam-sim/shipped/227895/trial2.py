#import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO
record = SeqIO.read("/var/esame/Desktop/sciprog-qcb-2021-11-05-exam/sciprog-qcb-2021-11-05-Surya-Hembrom-227895/small_seq.fasta", format="fasta")
print(record)
    #result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)




def computeStats(filename, show_output = True):
    raise Exception("TODO IMPLEMENT ME !")
    mydata=pd.Dataframe("/var/esame/Desktop/sciprog-qcb-2021-11-05-exam/sciprog-qcb-2021-11-05-Surya-Hembrom-227895/small_seq.fasta")
    print(mydata)


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