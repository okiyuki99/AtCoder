N = int(input())
S = [input() for i in range(N)]

# 'AB'の数を数える
cnt_ab = sum([s.count('AB') for s in S])

# L: 先頭が'B'、終わりが'A'の数を数える
cnt_b_a = sum([(s[0] == 'B') and (s[-1] == 'A') for s in S])

# M: 先頭が'B'、終わりが'A'じゃないの数を数える
cnt_b_na = sum([(s[0] == 'B') and (s[-1] != 'A') for s in S])

# N : 先頭が'B'じゃなく、終わりが'A'の数を数える
cnt_nb_a = sum([(s[0] != 'B') and (s[-1] == 'A') for s in S])

count = cnt_ab
if (cnt_b_a == 0): # MとNの数の小さい方の分だけ追加できる
    count += min(cnt_b_na, cnt_nb_a)
elif (cnt_b_na + cnt_nb_a == 0): # Lの個数 - 1個だけ追加できる
    count += (cnt_b_a - 1)
else:
    count += (cnt_b_a + min(cnt_b_na, cnt_nb_a))
print(count)
