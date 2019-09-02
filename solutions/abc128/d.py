import heapq
N,K = map(int, input().split())
*V, = map(int, input().split())
#N, K = 6, 4
#V = [-10, 8, 2, 1, 2, 6]
motimono = []
ans = []

if K >= N: # 操作回数のほうが大きいなら、全部取り出してから何個戻すかを考える
    K -= N
    heapq.heapify(V)
    ans.append(sum(V))
    for i in range(K):
        if len(V)>0:
            heapq.heappop(V)
        ans.append(sum(V))
    print(max(ans))

else:
    V *= 2 # 前後からの取り出しを楽にするためにこうしておく
    #print(V)
    for j in range(1,K+1): # 取り出す個数
        for i in range(N-j, N+1): # 何番目から取り出すか
            motimono = V[i:i+j]
            #print(str(j), str(i), motimono)
            ans.append(sum(motimono))
            #print(ans)
            heapq.heapify(motimono)
            for i in range(K-j): # 戻す個数
                if len(motimono)>0:
                    heapq.heappop(motimono)
                ans.append(sum(motimono))
    print(max(ans))
