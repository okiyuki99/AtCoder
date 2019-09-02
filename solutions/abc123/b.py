import numpy as np
S = [int(input()) for _ in range(5)]
amari = [10 if s % 10 == 0 else s % 10 for s in S]
t = 0
for i in range(5):
    ind = np.argsort(amari)[::-1][i]
    #print(ind, np.sort(amari)[::-1][i])
    if i == 4 :
        t += S[ind]
    else :
        t += S[ind] + (10 - amari[ind])
print(t)
