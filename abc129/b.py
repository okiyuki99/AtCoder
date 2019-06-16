N = int(input())
W = list(map(int, input().split()))
D = 9999999999999999999
for n in range(2,N) :
    S1 = sum(W[0:n])
    S2 = sum(W[n:N])
    #print(S1)
    #print(S2)
    d = abs(S1 - S2)
    if D > d :
        D = d
print(D)
