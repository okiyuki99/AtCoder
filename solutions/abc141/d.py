import heapq
#import itertools
import math
import numpy as np
#import sys

#N = int(input())
N, M = list(map(int, input().split()))
A = list(map(lambda x : int(x) * -1, input().split()))
#A = list(map(int, input().split()))
#A = list(np.array(A) * -1)

# リストA を ヒープで使う型に変換
heapq.heapify(A)
for i in range(M) :
    v = heapq.heappop(A)
    v = math.ceil(v / 2)
    heapq.heappush(A, v)
print(sum(A) * -1)


