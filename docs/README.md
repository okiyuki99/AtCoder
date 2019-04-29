## input 

### 1行に整数1つ

```py
# 10
N = int(input())
```

### 1行に整数複数

```py
# 5 6 8 10
A = list(map(int, input().split()))
```

### 複数行に渡る入力をリストに

```py
# H  WW
# S1
# ...
# SH
H, W = map(int, input().split())
S = [input() for _ in range(H)]
```

## str

```py
>>> s = 'abcdefg'
>>> s[0:2]
'ab'
>>> s[0:2 + 4]
'abcdef'
>>> s[0:2 + 2]
'abcd'
>>> s[:2]
'ab'
>>> s[:2] + 'xyz' + s[3:]
'abxyzdefg'
```
