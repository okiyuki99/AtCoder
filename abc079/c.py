from itertools import product
ABCD = list(input())
ops = ['+', '-']

for op in list(product(ops, ops, ops)) :
    if eval(ABCD[0] + op[0] + ABCD[1] + op[1] + ABCD[2] + op[2] + ABCD[3]) == 7 :
        print(str(ABCD[0] + op[0] + ABCD[1] + op[1] + ABCD[2] + op[2] + ABCD[3])+'=7')
        break

