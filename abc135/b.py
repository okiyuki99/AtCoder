N = int(input())
P = list(map(int,input().split()))
PS = sorted(P)
M = [i for i in range(N) if P[i] != PS[i]]
if len(M) <= 2 :
    print('YES')
else :
    print('NO')

