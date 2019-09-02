from itertools import accumulate

N = int(input())
M1 = list(map(int, input().split()))
M2 = list(map(int, input().split()))
M1a = list(accumulate(M1))
M2a = list(accumulate(M2[::-1]))
#print(M1a)
#print(M2a)

ans = -1
for i in range(N) :
    c = M1a[i] + M2a[N - 1 - i]
    if c > ans :
        ans = c
print(ans)
