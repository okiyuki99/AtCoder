# Ref : https://qiita.com/ct158603292321/items/11122ba8a5be3c97912b
import numpy as np
N, M = map(int, input().split())
L = []
for i in range(M):
    #a = list(map(int, input().split()))
    *a, = map(int, input().split())
    L.append(a[1:])
*P, = map(int, input().split())

ans = 0
for n in range(2 ** N):
    tmp = np.array([n >> s & 1 for s in range(N)])
    S = []
    for i in L :
        s = sum(tmp[np.array(i) - 1]) % 2
        S.append(s)
    if P == S :
        ans += 1
print(ans)
