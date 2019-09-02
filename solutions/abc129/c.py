# 配列からの探索をなくせば間に合う。
# Ref. https://ami-atcoder.hatenablog.com/entry/20190610/1560140980
MOD = 10 ** 9 + 7
n, m = [int(x) for x in input().split()]
pattern = [1]
broken = -1
brokencnt = 0
if brokencnt < m:
    broken = int(input())
    brokencnt += 1
for i in range(1, n + 1):
    if i == broken:
        pattern.append(0)
        if brokencnt < m:
            broken = int(input())
            brokencnt += 1
        continue
    if i == 1:
        pattern.append(pattern[i - 1])
    if i > 1:
        pattern.append((pattern[i - 1] + pattern[i - 2]) % MOD)
print(pattern[n])

# あってるけど、i in A がO(N)なので、TLE
# MOD = 10 ** 9 + 7
# n, m = [int(x) for x in input().split()]
# A = [int(input()) for i in range(m)]
# pattern = [1]
# for i in range(1, n + 1):
#     if i in A:
#         pattern.append(0)
#         continue
#     if i == 1:
#         pattern.append(pattern[i - 1])
#     if i > 1:
#         pattern.append((pattern[i - 1] + pattern[i - 2]) % MOD)
# print(pattern[n])

# import math
# import numpy as np
#
# # ref https://note.nkmk.me/python-math-factorial-permutations-combinations/
#
# def combinations_count(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
#
# N, M = map(int, input().split())
# A = [int(input()) for i in range(M)]
#
# diff = np.array(A)[1:] - np.array(A)[:-1]
# if any(diff == 1) :
#     print(0)
# else :
#     S = []
#     if M > 0 :
#         A.insert(0, 1)
#         A.insert(N-1, N + 1)
#         D = list(np.array(A)[1:] - np.array(A)[:-1] - 1)
#     else :
#         D = [N + 1]
#     R = []
#     for d in D :
#         P = d - 1
#         K = int(P / 2)
#         T = 1
#         for k in range(1, K+1) :
#             T += combinations_count(P - k, k)
#         R.append(T)
#     ans = R[0]
#     #print(R)
#     for r in R[1:] :
#         #print(ans)
#         ans = ans * r % (10 ** 9 + 7)
#     print(ans)
#

