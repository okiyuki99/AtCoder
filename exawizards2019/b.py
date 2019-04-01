# -*- coding: utf-8 -*-
N = int(input())
S = list(str(input()))
red_size = sum([s == 'R' for s in S])
blu_size = N - red_size
if red_size > blu_size :
    print("Yes")
else :
    print("No")
