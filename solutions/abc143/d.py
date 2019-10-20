#import heapq
#import itertools
#import math
#import numpy as np
#import sys
from bisect import bisect_left

N = int(input())
L = list(map(int, input().split()))
L = sorted(L)

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        ans += bisect_left(L, L[i] + L[j]) - j - 1
print(ans)

#for c in C :
#    L[c[1]] - L[c[0]]

#for c in C :
#    #print(c)
#    while True :
#        #print(L[c[1] + i])
#        if L[c[0]] + L[c[1]] > L[c[1] + i] :
#            ans += 1
#            i += 1
#        else :
#            i = 1
#            break

#        if c[1] + i > N - 1:
#            i = 1
#            break
#print(ans)


#a = [(x, y, z) for (x, y, z) in itertools.combinations(L, 3) if ((x+y) > z) and ((x+z) > y) and ((y+z) > x)]
#print(len(a))
