N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

taoshi_count = 0
for i in range(N):
    nokori = A[i] - B[i]
    if A[i] - B[i] >= 0 :
        taoshi_count += B[i]
    else :
        taoshi_count += A[i]
        nokori_power = abs(nokori)
        if A[i + 1] >= nokori_power :
            taoshi_count += nokori_power
            A[i + 1] -= nokori_power
        else :
            taoshi_count += A[i + 1]
            A[i + 1] = 0
print(taoshi_count)
