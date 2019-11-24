#import heapq
#import itertools
import math
#import numpy as np
import sys

A,B,X = list(map(int, input().split()))
#S = [input() for _ in range(H)]
#T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()

k = -1
for i in range(0,10) :
    n = (X - B * i) // A
    # c = int(''.join(['1'] * i)) * 9
    c = 10 ** i
    if n >= c :
        k = i
    else :
        break
    #[1] * iprint(c)
    #print(len(n))
if k == -1 :
    print(0)
    sys.exit()

#print(k)
if k == 9 :
    m = (X - B * k) // A
    if m > 1000000000 :
        print(1000000000)
        sys.exit()

m = (X - B * (k + 1)) // A
#print(m)
# c = int(''.join(['1'] * k)) * 9
# if(m < c) :
#     print(math.ceil(m))
#else :
print(math.floor(m))
