# Ref. https://oneminutepython.com/atcoder/abc126_d.html#%E7%B5%90%E6%9E%9C
from collections import deque

N = int(input())
S = [[]for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    S[u-1].append([v-1,w])
    S[v-1].append([u-1,w])
#print(S)

Node = [None]*N
Node[0] = True
queue = deque([0])
while queue != deque([]):
    #print(queue)
    #print(Node)
    p = queue.popleft()
    for u,w in S[p]:
        if Node[u] == None:
            queue.append(u)
            Node[u] = (Node[p])^(w % 2 == 1)
for i in range(N):
    print([0,1][Node[i]])
