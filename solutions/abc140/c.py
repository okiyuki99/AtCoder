#import sys
N = int(input())
B = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
A = [0] * N
A[0] = B[0]
A[N-1] = B[N-2]
for i in range(N - 2) :
    A[i+1] = min(B[i],B[i+1])
print(sum(A))
