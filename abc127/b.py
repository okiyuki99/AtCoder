r, D, x = map(int, input().split())
x2 = x
for i in range(10) :
    x2 = r * x2 - D
    print(x2)
