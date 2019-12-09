
#import heapq
import itertools
#import math
#import numpy as np
import sys

N = int(input())
D = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()
P = list(itertools.combinations(list(range(N)),2))
ans = 0
for p in P :
    #print(p)
    a = D[p[0]] * D[p[1]]
    ans += a
print(ans)
