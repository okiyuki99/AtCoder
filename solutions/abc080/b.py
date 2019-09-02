I = input()
S = list(I)
N = int(I)
if N % sum([int(i) for i in S]) == 0 :
    print('Yes')
else :
    print('No')
