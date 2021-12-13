def mem_limit(MB=None):
    import os
    if os.name == 'nt':
        print('WARNING: limiting memory on Windows is not supported')
        return
    
    import resource
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()            
            if str(sline[0]) == 'MemAvailable:':
                free_memory = int(sline[1])               
                break     
        if sline[2] != 'kB':
            raise Exception('Unrecognized memory unit:', sline[2])
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        if not MB:                    
            MB = (free_memory // 1024) // 2  
        print('Free mem:', free_memory//1024, 'MB', 
              ' Limiting to:', MB, 'MB')
        resource.setrlimit(resource.RLIMIT_AS, (MB *1024 * 1024, hard))

mem_limit()

#####
import mem_limit

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO

fn = "data_reduced.agp"

def computeStats(filename, show_output = True):
    DF = pd.read_csv(filename, sep="\t")
    
    if show_output == True:
        entries = DF.shape[0]
        scaffolds = len(DF["ScaffID"].value_counts())
        print("The file contains {} entries".format(entries))
        print("... {} scaffolds".format(scaffolds))

        contigs = DF[DF["contig"] != "500"]["contig"].count()
        bases = DF[DF["c_end"] != "yes"]["c_end"].astype(int).sum()
        print("... {} contigs (tot. size: {} bases)".format(contigs, bases))
        
        gaps = DF[DF["type"] == "N"]["type"].count()
        gapsN = DF[DF["type"] == "N"]["contig"].astype(int).sum()
        print("... {} gaps (tot.size {} bases".format(gaps, gapsN))

        #boxplot of the number of contigs per scaffold:
        scaffgr = DF[["ScaffID", "contig"]].groupby("ScaffID")
        L = []
        for name, df in scaffgr:
            L.append(int(len(df))) #num di scaffold per df
        
        A = pd.Series(L)
        
        A.plot(kind = "box", label = "contig")
        plt.show()
        plt.close()
    else:
        print(DF.head(5)) #ok    

    return DF





#Try:
fn = "data_reduced.agp"
scaffDF = computeStats(fn) #ok
scaffDF = computeStats("small.agp", show_output = False) #ok


'''printSequence(scaffDF,"my_scaff","small_seq.fasta")
print("")
''''''printSequence(scaffDF,"my_scaff2","small_seq.fasta")
print("")
printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
print("")
printSequence(scaffDF,"scaffold3","small_seq.fasta")
'''
