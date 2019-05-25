S = list(input())
S1 = ''.join(S[0:2])
S2 = ''.join(S[2:4])

if int(S1) >= 1 and int(S1) <= 12 :
    if int(S2) >= 1 and int(S2) <= 12 :
        print('AMBIGUOUS')
    else :
        print('MMYY')

else :
    if int(S2) >= 1 and int(S2) <= 12 :
        print('YYMM')
    else :
        print('NA')
