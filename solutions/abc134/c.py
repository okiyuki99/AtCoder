import numpy as np
N = int(input())
A = [int(input()) for _ in range(N)]
MA = max(A)
ans = [MA] * N
MAI = np.argmax(np.array(A))
A[MAI] = 1
MA2 = max(A)
ans[MAI] = MA2
for a in ans :
    print(a)
