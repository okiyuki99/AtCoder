import sys
from itertools import combinations
L, R = map(int, input().split())
if R - L >= 2018 :
    print(0)
    sys.exit()
LM = L % 2019
RM = R % 2019
if RM < LM :
    print(0)
else :
    S = range(LM, RM+1)
    SC = list(combinations(S, 2))
    print(min([s[0] * s[1] % 2019 for s in SC]))
    #print(SC)
    #print((L * (L+1)) % 2019)
