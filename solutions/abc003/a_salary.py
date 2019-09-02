# -*- coding: utf-8 -*-
N = int(input())
salary = 0
for n in range(1,N+1) :
    salary += n * 10000 * 1 / N
print(int(salary))
