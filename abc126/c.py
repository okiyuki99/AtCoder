import math
N, K = map(int, input().split())
total = 0.0

for n in range(1,N+1) :
    if n >= K :
        total += 1.0 / N
    else :
        total += (1.0 / N) * 0.5 ** math.ceil(math.log2(1.0 * K / n))
print(total)



