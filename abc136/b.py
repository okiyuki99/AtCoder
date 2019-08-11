N = int(input())
#A, B = list(map(int,input().split()))
#A = [int(input()) for _ in range(N)]
count = 0
for i in range(1,N+1) :
    if len(str(i)) % 2 != 0 :
        count += 1
print(count)
