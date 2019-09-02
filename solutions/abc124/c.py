S = input()
l = len(S)
c1 = ''.join(['0' if i %2 == 0 else '1' for i in range(l)])
c2 = ''.join(['1' if i %2 == 0 else '0' for i in range(l)])
x = sum(a == b for a, b in zip(S, c1))
y = sum(a == b for a, b in zip(S, c2))
if x > y :
    print(y)
else :
    print(x)
