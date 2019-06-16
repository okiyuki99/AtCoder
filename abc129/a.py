P,Q,R = map(int, input().split())
PQR = [P + Q, Q + R, P + R]
print(min(PQR))
