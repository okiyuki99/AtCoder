#import heapq
#import itertools
#import math
#import numpy as np
#import sys

N = int(input())
S = list(input())
#A,B = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()
ALPHA = [chr(ord('A') + i) for i in range(26)]

for i in range(len(S)):
    ind = ALPHA.index(S[i])
    if int(ind) + N > 25 :
        S[i] = ALPHA[int(ind) + N - 26]
    else :
        S[i] = ALPHA[int(ind) + N]
print(''.join(S))