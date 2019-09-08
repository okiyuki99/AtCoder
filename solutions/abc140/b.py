#import sys
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
pre = -1
man = 0
for i in A:
    man += B[i - 1]
    if pre == i - 1 :
        man += C[pre - 1]
    pre = i
print(man)

