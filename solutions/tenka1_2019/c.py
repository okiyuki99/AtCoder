from itertools import accumulate

N = int(input())
S = input()

B = [0] * N
W = [0] * N

for i, s in enumerate(S):
    if s == '#':
        B[i] = 1
    else :
        W[i] = 1

B = [0] + B
B = list(accumulate(B)) # -- 位置を左から進めて、左側にある黒の数
W = [0] + W[::-1]
W = list(accumulate(W))[::-1] # -- 位置を左から進めて、右側にある白の数

ans = []
for i in range(N+1):
    ans.append(B[i] + W[i])
print(min(ans))
