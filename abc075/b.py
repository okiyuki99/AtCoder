H,W = map(int,input().split())
mas = [input() for i in range(H)]
dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

ans = []
for i in range(H) :
    ans.append(['#'] * W)

for h in range(H) :
    for w in range(W) :
        c = 0
        if mas[h][w] == '#':
            continue
        for i in range(9) :
            if w + dx[i] < 0 or h + dy[i] < 0 or w + dx[i] > W - 1 or h + dy[i] > H - 1:
                continue
            if mas[h+dy[i]][w+dx[i]] == '#' :
                c += 1
        ans[h][w] = c

for a in ans :
    b = map(str, a)
    print(''.join(b))
        
