# -*- coding: utf-8 -*-
k = int(input())
gu = 0
ki = 0
for i in range(1,k+1) :
    if i % 2 == 0 :
        gu += 1
    else :
        ki += 1
print(gu * ki)
