#import heapq
import itertools
import math
#import numpy as np
#import sys

N = int(input())
#S = list(input())
#A = list(map(int, input().split()))
#S = [input() for _ in range(H)]
T = [list(map(int,input().split())) for _ in range(N)]
#sys.exit()
#print(T)

K = 0
C = list(itertools.combinations(list(range(N)),2))
for c in C :
    #print(c)
    k = (T[c[0]][0] - T[c[1]][0]) * (T[c[0]][0] - T[c[1]][0]) + (T[c[0]][1] - T[c[1]][1]) * (T[c[0]][1] - T[c[1]][1])
    k = math.sqrt(k)
    K += k
#print(K)
kaisu = (N - 1) * math.factorial(N) / len(C)
#print(kaisu)
print(K * kaisu  / math.factorial(N))