from math import sqrt, log10
ans = 100000000000000000
N = int(input())
for i in range(1, int(sqrt(N))+1) :
    A = i
    B = int(N / A)
    if N % A == 0:
        if A >= B :
            m = int(log10(A)) + 1
        else :
            m = int(log10(B)) + 1
        if m < ans :
            ans = m
            #print(ans)
            #print('{0},{1}'.format(A,B))
print(ans)

