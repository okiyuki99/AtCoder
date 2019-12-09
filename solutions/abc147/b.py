#import heapq
#import itertools
#import math
#import numpy as np
#import sys

S = list(input())
#A,B,C = list(map(int, input().split()))
# S = [input() for _ in range(H)]
# T = [list(map(int,input().split())) for _ in range(N)]
# sys.exit()
ans = 0
if len(S) % 2 == 0 :
    h = int(len(S) / 2)
    s1 = S[0:h]
    s2 =  S[::-1][0:h]
    for i in range(h) :
        if s1[i] != s2[i] :
            ans += 1

else :
    h = int((len(S) - 1) / 2)
    s1 = S[0:h]
    s2 =  S[::-1][0:h]
    for i in range(h) :
        if s1[i] != s2[i] :
            ans += 1

print(ans)