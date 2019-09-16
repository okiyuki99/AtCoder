#import heapq
#import itertools
#import math
#import numpy as np
import sys

S = list(input())
#A = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
for i in range(len(S)) :
    if i % 2 == 1 :
        if S[i] in 'LUD' :
            pass
        else :
            print('No')
            sys.exit()
    elif i % 2 == 0 :
        if S[i] in 'RUD' :
            pass
        else :
            print('No')
            sys.exit()
print('Yes')

