# -*- coding: utf-8 -*-
N,A,B= list(map(int, input().split()))
S = 0
for n in range(1,N+1) :
    li = list(str(n))
    s = sum([int(i) for i in li])
    if s >= A and s <= B :
        S += n
print(S)
