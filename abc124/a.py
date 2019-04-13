A,B = map(int, input().split())
coin = 0
if A > B :
    coin = A
    A -= 1
else :
    coin = B
    B -= 1
if A > B :
    coin += A
else :
    coin += B
print(coin)
