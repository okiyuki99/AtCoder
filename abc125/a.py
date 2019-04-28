A, B, T = map(int, input().split())

bis = 0
time = 0
while True :
    time += A
    if time < T + 0.5 :
        bis += B
    else :
        break
print(bis)
