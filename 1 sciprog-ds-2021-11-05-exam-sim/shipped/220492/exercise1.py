
import mem_limit

def find_missing(S):
    if len(S)==0:
        print("Warning: list is empty. Returning None")
        return None
    else:
        S1=S.copy()
        for i in S:
            if i <0:
                print(f"Warning {i} is <0. Ignoring it.")
                S1.remove(i)
            elif i==0: S1.remove(i)
        S1=set(S1)
        S2=list(S1)
        S2.sort()
        myS=[]
        for i in range(len(S2)):
            if i==0 and S2[i]!=1:
                j=1
                while j!= S2[i] and j<S2[-1]:
                    myS.append(j)
                    j+=1
            elif i!=len(S2)-1:
                k=S2[i]
                while k+1!=S2[i+1] and k<S2[-1]:
                    myS.append(k+1)
                    k+=1
        return myS


S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
