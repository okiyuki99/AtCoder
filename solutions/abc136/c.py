import sys
N = int(input())
H = list(map(int,input().split()))
for i in range(N) :
    if i == 0 :
        H[i] -= 1
    else :
        if H[i-1] == H[i] :
            pass
        elif H[i-1] <= H[i] - 1  :
            H[i] -= 1
        elif H[i-1] > H[i] :
            print('No')
            sys.exit()
print('Yes')


