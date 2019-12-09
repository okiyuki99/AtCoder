#import heapq
#import itertools
#import math
#import numpy as np
#import sys

N = int(input())
A = list(map(int, input().split()))
#S = [input() for _ in range(H)]
# T = [list(map(int,input().split())) for _ in range(N)]
# sys.exit()
#print(A)
ans = 0
for i in range(1,N) :
    for j in range(i+1, N+1) :
        #print(i,j)
        ans += A[i - 1] ^ A[j - 1]

# TLE orz
print(ans % (10 ** 9 + 7))