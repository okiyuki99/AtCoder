# URL https://refining-process.hatenablog.com/entry/2019/07/21/005322
N = int(input())
a = list(map(int,input().split()))

b = [0 for i in range(N)]

def check(i):
    cnt = 0
    n = i
    while n <= N:
        cnt += b[n-1]
        n += i
    return cnt

for i in range(N-1, -1, -1):
    if (a[i] + check(i+1)) % 2 == 1:
        b[i] = 1

ans = []
cnt = 0
for i in range(N):
    if b[i] == 1:
        cnt += 1
        ans.append(i+1)

print(cnt)
L = [str(int(i)) for i in ans]
print(' '.join(L))

# N = int(input())
# A = list(map(int, input().split()))
# Ab = [0] * N
# for i in range(1,N+1):
#     Ab[i-1] = sum([A[j-1] for j in range(1,N+1) if j % i == 0])
# print(Ab)
# ans = [0] * N
# for i, a in enumerate(Ab[::-1]) :
#     if i <= N / 2:
#         ans[i] = a
#     else :
#     print(a)

