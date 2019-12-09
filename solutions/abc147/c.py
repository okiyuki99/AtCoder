#import heapq
#import itertools
#import math
#import numpy as np
#import sys

N = int(input())
A = []
X = []
for i in range(N) :
    A.append(int(input()))
    x = [list(map(int,input().split())) for _ in range(A[i])]
    X.append(x)
#print(A)
#print(X)

# bit all search
P = []
for i in range(2 ** N): # 全パターン数を1つずつ作っていく
    pat = [0] * N
    for j in range(N): 
        if ((i >> j) & 1) : #もとの数iを2進数表記でみて、1が立ってる箇所をチェックしていく  
            pat[N - 1 - j] = 1 
    P.append(pat)
#print(P)

# 正直 or 偽物の条件にマッチするやつチェック
ans = 0
flag = 'Y'
for p in P :
    for i in range(N) :
        if p[i] == 1 : # 正直者である人の意見を見に行く
            for x in X[i] :
                if x[1] != p[x[0]-1] :
                    flag = 'N'
    if flag == 'Y' : # flag = Y を維持したなら矛盾なしということで判定
        c = sum(p)
        if c > ans :
            ans = c
    flag = 'Y' # 初期化
print(ans)
