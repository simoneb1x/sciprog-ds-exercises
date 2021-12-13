
import mem_limit

def find_missing(S):
    N = len(S)
    #print(N)
    L = []
    if N == 0:
        print("Warning: empty list")
        return None
    else: 
        N = [x for x in S if x < 0]
        for i in range(len(N)):
            print(f"Warning: {N[i]} is negative: ignore it")
        P = [x for x in S if x >= 0]
        #print(P)
        L = [x for x in range(1,max(P)) if x not in S]
        return L


S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)

            
#        S.sort()
#        if S[0] <= 0 : 
#            print("Warning, {} ".format())
#        else:
#            L = [x for x in range(1,N) if x not in S]
