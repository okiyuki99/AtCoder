N = int(input())
i = 0
j = 0
cnt = 0
while True :
    K = i * 4 + j * 7
    if K == N :
        print('Yes')
        break
    elif N < K and cnt == 0 :
        print('No')
        break
    elif N < K :
        j += 1
        i = 0
        cnt = 0
    else :
        i += 1
        cnt += 1

