K, S = map(int, input().split())
cnt = 0
for x in range(S + 1) :
    if x > K :
        continue
    for y in range(S - x + 1) :
        if y > K :
            continue
        z = S - x - y
        if z > K:
            continue
        cnt += 1
print(cnt)
