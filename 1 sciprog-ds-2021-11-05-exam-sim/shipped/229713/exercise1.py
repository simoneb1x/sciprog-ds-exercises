
import mem_limit

def find_missing(S):

    if not S:
        return "Warning: list is empty. Returning None"
    
    unique_vals = []

    for val in S: 
        if val < 0:
            print(f"Warning: {val} is <0. Ignoring it.")
        if val not in unique_vals:
            unique_vals.append(val)

    missing_vals = []

    for mis in range(1, max(unique_vals)):
        if mis not in unique_vals:
            missing_vals.append(mis)
    
    return missing_vals




S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
