A,B,C,D = map(int, input().split())
s, e = 0,0
if C > A:
    s = C
else:
    s = A
if D > B :
    e = B
else :
    e = D
if s > e :
    print(0)
else :
    print(e - s)
