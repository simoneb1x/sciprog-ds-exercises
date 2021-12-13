
import mem_limit

def find_missing(S):
    S.sort()
    L=[] 
    N=len(S)
    L4=[]
    L2=S
    if N==0:
        print("Warning : list is empty. Returning None")
        return None
    else:
        for i in range(len(S)):    
            if S[i]<0:
                print(f"Warning {S[i]} is <0. Ignoring it ")

                L2=S.remove(S[i])
                print(L2)
                L3= [x for x in range(L2[0], L2[-1]+1)]
                if L3[i] not in L2:
                    L.append(L3[i])
                return L4

                
            else:
                L1= [x for x in range(S[0], S[-1]+1)]
                if L1[i] not in S:
                    L.append(L1[i])
            return L


   



S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
