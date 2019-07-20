import math
from itertools import combinations
N, D = map(int, input().split())
X = [list(map(int , input().split())) for i in range(N)]
P = list(combinations(range(1,N+1), 2))
#print(X)
count = 0
for p in P :
    x = X[p[0] - 1]
    y = X[p[1] - 1]
    #print(x,y)
    ans = 0
    for d in range(D) :
        ans += (x[d] - y[d]) * (x[d] - y[d])
    ans = math.sqrt(ans)
    #print(ans)
    if ans.is_integer() :
        count += 1
print(count)
