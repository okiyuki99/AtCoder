# -*- coding: utf-8 -*-
A, B = map(int, input().split())
S = list(str(input()))
Q = [list(map(str, input().split())) for _ in range(B)]
#print(A)
#print(B)
#print(S)
#print(Q)
#print("===")
golem = [1 for _ in range(A)]
#print(golem)
for b in range(B) :
    #print("===")
    #print(b)
    q = Q[b]
    t = [s == q[0] for s in S]
    ind = [i for i, x in enumerate(t) if x]
    #print(ind)
    for i in ind :
        if golem[i] >= 1 :
            golem[i] -= 1
            if q[1] == 'L' :
                if i - 1 >= 0 :
                    golem[i - 1] += 1
                else :
                    pass
            else :
                if i + 1 <= A - 1  :
                    golem[i + 1] += 1
                else :
                    pass
    #print(golem)
print(sum(golem))
