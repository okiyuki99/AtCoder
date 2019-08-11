#N = int(input())
A, B, C = list(map(int,input().split()))
#A = [int(input()) for _ in range(N)]
D = A - B
C = C - D
if C < 0 :
    print(0)
else :
    print(C)
