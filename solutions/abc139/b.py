#import sys
A, B = list(map(int,input().split()))
count = 0
tukaeru = A
if B > 1 :
    while True :
        count += 1
        if tukaeru >= B :
            break
        else :
            tukaeru += A -1
print(count)
