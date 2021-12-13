
import mem_limit
#Given a list of posi!ve integers (possibly repeated and unsorted) in the range [1,N],
#write a func!on that finds the missing values and returns them as a list. Note that the
#func!on should not crash if the list is empty. A warning should also be printed in case
#the user by mistake had nega!ve numbers in the list.

def find_missing(l):
    if len(l)==0:
        print('Warning: list is empty. Returning None')
        return None
    s=list(set(l))
    for el in l:
        if el<0:
            print('Warning {} is <0. Ignoring it.'.format(el))
            if el in s:
                s.remove(el)
    s.sort()
    ref=list(range(s[0],s[-1]))
    for el in s:
        if el not in ref:
            pass
        else:
            ref.remove(el)
    return ref
        
#    raise Exception("TODO IMPLEMENT ME !")


S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
