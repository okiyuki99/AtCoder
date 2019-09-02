#N = int(input())
A, B = list(map(int,input().split()))
#A = [int(input()) for _ in range(N)]
i = (B - A) / 2
if i.is_integer() :
    print(B - int(i))
else :
    print('IMPOSSIBLE')
