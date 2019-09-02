# -*- coding: utf-8 -*-
N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse = True)
A, B = 0, 0
while N != 0 :
    A += a.pop(0)
    N -= 1
    if N == 0 :
         break
    B += a.pop(0)
    N -= 1
print(A-B)
