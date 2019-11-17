#import heapq
import itertools
#import math
#import numpy as np
import sys

N = int(input())
S = input()
#D = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()
a = S[0:int(N/2)]
b = S[int(N/2):N]
if a == b :
    print('Yes')
else :
    print('No')
