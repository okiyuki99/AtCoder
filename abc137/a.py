#import sys
#N = int(input())
A, B = list(map(int,input().split()))
#A = [int(input()) for _ in range(N)]
a1 = A + B
a2 = A - B
a3 = A * B
print(max(a1, a2, a3))
#sys.exit()
