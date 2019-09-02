# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))
count = 0
while True : 
    is_even = all([a % 2 == 0 for a in A])
    if is_even == False :
        break
    A = [a / 2 for a in A]
    count += 1
print(count)
