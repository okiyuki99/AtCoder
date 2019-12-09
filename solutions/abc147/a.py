#import heapq
#import itertools
#import math
#import numpy as np
#import sys

A,B,C = list(map(int, input().split()))
# S = [input() for _ in range(H)]
# T = [list(map(int,input().split())) for _ in range(N)]
# sys.exit()
if A + B + C >= 22 :
    print('bust')
else :
    print('win')