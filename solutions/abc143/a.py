#import heapq
#import itertools
#import math
#import numpy as np
#import sys

#S = input()
A,B = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()
ans = A - 2*B
if(ans <= 0) :
    print(0)
else :
    print(ans)
