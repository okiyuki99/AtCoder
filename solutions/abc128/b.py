N = int(input())
SP = [list(input().split()) + [i+1] for i in range(N)]
SP = [[sp[0], int(sp[1]), sp[2]] for sp in SP]
#SP2 = [SP[i] + [i] for i in range(N)]
SP = sorted(SP, key = lambda x : x[1], reverse=True)
SP = sorted(SP, key = lambda x : x[0])
#SP = sorted(SP, key = lambda x : x[0]), key = lambda x : x[1], reverse=True)
#print(SP)
ans = [sp[2] for sp in SP]
for a in ans :
    print(a)
