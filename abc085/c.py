# -*- coding: utf-8 -*-
N,Y = list(map(int, input().split()))
total = 0
find = False
for x in range(N+1) :
    a = 10000 * x
    for y in range(N + 1 - x) :
        b = 5000 * y
        z = N - x - y
        c = 1000 * z
        total = a + b + c
        if total == Y :
            print(x, y, z)
            find = True
            break
    if find :
        break
if not find :
    print(-1,-1,-1)
