
import mem_limit

def find_missing(S):
    if not S:
        print("Warning: list is empty. Returning None")
        return None
    S=sorted(S)
    if S[0]<=0:
        j=0
        while j<len(S) and S[j]<0:
            print("Warning {} is <0. Ignoring it.".format(S[j]))
            j+=1
    l=[]
    for i in range(1,max(S)):
        if i not in S:
            l.append(i)
    return l


S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
