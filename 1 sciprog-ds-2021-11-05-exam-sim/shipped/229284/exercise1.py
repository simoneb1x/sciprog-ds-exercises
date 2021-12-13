
import mem_limit

def find_missing(S):
    min=0
    miss=[]
    if len(S)==0:
        print('Warning: list is empty. Returning None')
        return None
    else:
        for i in S:
            if i>min:
                min=i
            elif i<0 :
                print('Warning:',i,'< 0, ignoring it')    
        for i in range(1,min+1):
            if i not in S:
                miss.append(i)
        return miss




S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
