#import heapq
#import itertools
#import math
#import numpy as np
#import sys

S = input()
# A,B = list(map(int, input().split()))
# S = [input() for _ in range(H)]
# T = [list(map(int,input().split())) for _ in range(N)]
# sys.exit()
if S == 'SAT' :
    print(1)
elif S == 'MON' :
    print(6)
elif S == 'TUE' :
    print(5)
elif S == 'WED' :
    print(4)
elif S == 'THU' :
    print(3)
elif S == 'FRI' :
    print(2)
elif S == 'SUN' :
    print(7)
