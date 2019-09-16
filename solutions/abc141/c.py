#import heapq
#import itertools
#import math
#import numpy as np
#import sys

#N = int(input())
N, K, Q = list(map(int, input().split()))
A = [int(input()) for _ in range(Q)]
S = [0] * N
for i in A :
    S[i - 1] += 1
for s in S :
    if s > Q - K :
        print('Yes')
    else :
        print('No')


#for i in range(1,N+1) :
#    s = 0
#    for a in A :
#        if i == a :
#            s += 1
#    if s > Q - K :
#        print('Yes')
#    else :
#        print('No')


#T = [list(map(int,input().split())) for _ in range(N)]
#H = [K] * N
#print(A)
#print(H)
#for a in A :
#    for i in range(N) :
#        if i == int(a) :
#            pass
#        else :
#            H[i -1] -= 1
#for h in H :
#    if h > 0 :
#        print('Yes')
#    else :
#        print('No')
#ans = ['Yes' if h > 0 else 'No' for h in H]
#for a
#print(ans)
