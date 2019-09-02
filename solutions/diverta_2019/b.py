R,G,B,N = map(int, input().split())
count = 0
for r in range(N // R + 1) :
    for g in range((N - r*R) // G + 1) :
        if (N - r*R - g*G) %B == 0 :
            count += 1
print(count)
