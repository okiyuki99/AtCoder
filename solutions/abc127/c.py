import collections
N, M = map(int, input().split())
S = [list(map(int, input().split())) for i in range(M)]
smax = max([s[0] for s in S])
smin = min([s[1] for s in S])
if smin - smax + 1 >= 0 :
    print(smin - smax + 1)
else :
    print(0)

#S2 = [set(range(s[0], s[1] + 1)) for s in S]
#S3 = set.intersection(*S2)
#print(len(S3))

#ans = set(range(S[0][0], S[0][1] + 1))
#for s in S[1:] :
#    a = set(range(s[0], s[1] + 1))
#    ans = ans & a
#    if len(ans) == 0 :
#        break
#print(len(ans))
