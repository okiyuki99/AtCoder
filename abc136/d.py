memo = {}
same = 0
S = input()
C = [1] * len(S)
CN = [0] * len(S)
for i in range(1, 10 ** 100) :
    for j in range(len(S)) :
        if C[j] > 0 and S[j] == 'R' :
            CN[j + 1] += C[j]
            C[j] -= 0
        elif C[j] > 0 and S[j] == 'L' :
            CN[j - 1] += C[j]
            C[j] -= 1
    C = CN
    CN = [0] * len(S)
    P = ' '.join(map(str,C))
    if P in memo.values() :
        if memo[i-1] == P :
            same = 1
        else :
            same = 0
        break
    else :
        memo[i] = P

if same == 1 :
    ans = memo[len(memo)]
else :
    amari = (10 ** 100 - len(memo)) % 2
    if amari == 0:
        ans = memo[len(memo)]
    else:
        ans = memo[len(memo) - 1]
print(ans)

#print(memo)
#print(len(memo))
#print(same)

#print(amari)

