import itertools
H,W = map(int,input().split())
mas = [input() for _ in range(H)]
ans = 0
for i, j in itertools.product(range(H), range(W)):
    if mas[i][j] == '.':
        pass
    else :
        if i == 0 : # top row
            if j == W - 1 : # right edge
                if mas[i][j-1] == '.' and mas[i][j+1] == '.' :
                    print('No')
                    #print(1)
                    ans = 1
                    break
            elif j == 0 : # left edge
                if mas[i+1][j] == '.' and mas[i][j+1] == '.' :
                    print('No')
                    #print(2)
                    ans = 1
                    break
            else :
                if mas[i][j - 1] == '.' and mas[i + 1][j] == '.' and mas[i][j + 1] == '.':
                    print('No')
                    #print(3)
                    ans = 1
                    break
        elif i == H - 1 : # bottom row
            if j == W - 1 : # right edge
                if mas[i-1][j] == '.' and mas[i][j-1] == '.' :
                    print('No')
                    #print(4)
                    ans = 1
                    break
            elif j == 0 : # left edge
                if mas[i-1][j] == '.' and mas[i][j-1] == '.' :
                    print('No')
                    #print(6)
                    ans = 1
                    break
            else :
                if mas[i-1][j] == '.' and mas[i][j + 1] == '.' and mas[i][j - 1] == '.':
                    print('No')
                    #print(5)
                    ans = 1
                    break
        else : # middle row
            if j == W - 1 : # right edge
                if mas[i-1][j] == '.' and mas[i][j-1] == '.' and mas[i+1][j] == '.' :
                    print('No')
                    #print(7)
                    ans = 1
                    break
            elif j == 0 : # left edge
                if mas[i+1][j] == '.' and mas[i-1][j] == '.' and mas[i][j+1] == '.' :
                    print('No')
                    #print(8)
                    ans = 1
                    break
            else :
                if mas[i-1][j] == '.' and mas[i + 1][j] == '.' and mas[i][j - 1] == '.' and mas[i][j + 1] == '.':
                    print('No')
                    #print(9)
                    ans = 1
                    break
if ans == 0 :
    print('Yes')
