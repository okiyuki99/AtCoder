W, H, x, y = map(int, input().split())
M = W * H / 2
J = 0
if x == W / 2 and y == H / 2 :
    J = 1
print(M, J)
