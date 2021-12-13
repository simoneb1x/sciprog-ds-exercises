
import mem_limit

def find_missing(S):
    if len(S)==0:
        print("Warning: list is empty. Returning None")
        return None 

    nv=[i for i in S if i<0]
    if len(nv)!=0:
        for n in nv:
            print(f"Warning {n} <0. Ignoring it.")

    L = [i for i in range(1,max(S)+1) if i not in S]
    
    return L


S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
