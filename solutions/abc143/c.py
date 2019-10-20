#import heapq
#import itertools
#import math
#import numpy as np
#import sys

N = int(input())
S = list(input())
#A = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()

mae = ''
ans = 0
for s in S :
    if s == mae :
       pass
    else :
        ans += 1
    mae = s
print(ans)
