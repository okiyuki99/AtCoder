# Ref : https://qiita.com/cocet33000/items/a81a3379fefcc3ffcaf1
import heapq
#N = int(input())
N, M = list(map(int,input().split()))
jobs = [[] for _ in range(M)]
#AB = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    d, r = list(map(int, input().split()))
    if d-1 < M:
        jobs[d-1].append(-r)

#print(jobs)
ans = 0
heap = []

for i in range(M) :
    #print(jobs[:i])

    for hou in jobs[i] :
        heapq.heappush(heap, hou)
    if len(heap) > 0 :
        thou = heapq.heappop(heap)
        ans += -thou

print(ans)

# print(AB)
# AB = sorted(AB, key = lambda x : x[1], reverse=True)
# AB = sorted(AB, key = lambda x : x[0])
# print(AB)
# hou = 0
# nokori = M
#
# for i in range(N)  :
#     ab = AB[i]
#     if ab[0] <= nokori :
#         hou += ab[1]
#         nokori -= 1
# print(hou)

