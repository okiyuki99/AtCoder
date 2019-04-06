S = [int(input()) for _ in range(5)]
k = int(input())
mi = min(S)
ma = max(S)
if ma - mi > k:
    print(':(')
else :
    print('Yay!')
