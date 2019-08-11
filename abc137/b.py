#import sys
#N = int(input())
K, X = list(map(int,input().split()))
#A = [int(input()) for _ in range(N)]

T = [str(i) for i in range(X - (K-1), X + K) if i >= -1000000 and i <= 10000000]
print(' '.join(T))


#sys.exit()
