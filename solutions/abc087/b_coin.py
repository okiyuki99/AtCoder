a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for aa in range(a+1) :
	for bb in range(b+1) :
		for cc in range(c+1):
			ans = aa * 500 + bb * 100 + cc * 50
			if ans == x :
				count += 1
print(count)
