from itertools import accumulate
N, X = map(int, input().split())
L = map(int, input().split())
LA = list(accumulate(L))
C = sum([i <= X for i in LA])
print(C + 1)
