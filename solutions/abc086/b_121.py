import math
a, b = input().split()
c = int(a+b)
d = math.sqrt(c)

if d * d == c :
	print("Yes")
else :
	print("No")