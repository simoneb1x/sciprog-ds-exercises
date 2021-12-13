
import mem_limit

def find_missing(S):
    if len(S) == 0:
        print("Warning: list is empty. Returning None")
        return None

    for num in S:
        if num < 0:
            print("Warning {} is < 0. Ignore it".format(num))
            while num in S:
                S.remove(num) 

    S.sort()
    max = S[-1]
    min = S[0]
    ver = list(range(min, max))
    missing = [n for n in ver if n not in S]    

    return missing


S = [1, 9, 7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)

