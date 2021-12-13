
import mem_limit

def find_missing(S):
	M = []
	length = len(S)
	if length == 0: #warning empty list
		print("Warning: list is empty. Returning None")
	else:
		L = list(range(max(S)))
		S.sort()
		if L == S:
			return None
		for n in S:
			if n < 0: #warning negative element
					print("Warning {} is < 0. Ignoring it.".format(n))
			else:
				for i in L:
					if i not in S:
						M.append(i)
					elif i in S:
						continue
				return M		



S = [1,9,7, 7, 4, 3, 3, 3]
S1 = list(range(10))
print(find_missing(S))
print(find_missing(S1))
print(find_missing([]))
S2 = [1, -72, 4, -3, -3, 3,10]
M = find_missing(S2)
print(M)
