A, B, C, D, E, F = map(int, input().split())
memo = {}

for a in range(31):
    for b in range(31):
        for c in range(101):
            for d in range(101):
                w = (100 * A) * a + (100 * B) * b
                s = C * c + D * d
                if w == 0:
                    break
                if w + s > F:
                    break
                else:
                    if w / 100 * E >= s:
                        density = 100 * s / (w + s)
                        memo[a, b, c, d] = density

max_v = max(memo.values())

for k, v in memo.items():
    if v == max_v:
        print((100 * A) * k[0] + (100 * B) * k[1] + C * k[2] + D * k[3], C * k[2] + D * k[3])
        break
