
def find_missing(s,s2,s3):
    #s=[]; s2=[]; s3=[]
    S1=[]
    S1 = list(range(10))
    for i,j in range(10):
        if S1[i] == S[j]:
           print("not missing")
        else:
            s.append(S1[i])
            print("Warning: list is empty. Returning None")
        if S1[i] == S2[j]:
            print("not missing")
        else:
            s2.append(S1[i])
        if S1[i] == S3[j]:
            print("not missing")
        else:
            s3.append(S1[i])
    return S1

S = [1,9,7, 7, 4, 3, 3, 3]
S2 = [1, -72, 4, -3, -3, 3,10]
S3= ([])
x= find_missing(S, S2, S3)
print(x)