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

### sys.stdin.readline
10^5 超える入力なら使ったほうが早い

```py
import sys
input = sys.stdin.readline

a = input()
b = list(input())
c = list(input())[:-1]
# or c = list(input().strip())
print(a)
print(b)
print(c)

<input>
abc
abc
abc
<output>
abc
['a', 'b', 'c', '\n']
['a', 'b', 'c']
```

## math

```py
>>> 321 % 100 # mod = 余り計算
21
>>> 321 // 100 # 商だけ
3
>>> 2 ** 3 # 乗
8
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

## list

```py
>>> a = ['a', 'b', 'c']

# 最後の要素アクセス
>>> a[-1]
'c'

# 最後の要素抜く
>>> a[:-1]
['a', 'b']

# 反転
>>> a[::-1]
['c', 'b', 'a']

```

## range

逆向き

```py
for i in range(5, 1, -1):
    print(i)
---
5
4
3
2
```

## X倍のindexを得る

```py
i = 3
n = i
while n <= 10:
    n += i
    print(n)
---    
6
9
12
```

## sort

### 複数のkeyを持ったリストをソートさせる（2番目が大きい順なかで、1番目が大きい順にとか）

```py
# 参考 : https://atcoder.jp/contests/abc128/tasks/abc128_b
print(AB)
AB = sorted(AB, key = lambda x : x[0], reverse=True)
AB = sorted(AB, key = lambda x : x[1], reverse=True)
print(AB)

>>> [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3]] # 入力はこんなの
>>> [[1, 4], [2, 3], [1, 3], [1, 2], [2, 1]] # 2番目が大きい順でかつ、同じ値のものは、1番目が大きい順になってる
```

### X番目に大きいのを求めるもsortがまずまず速い

### ある文字列のソート

```
>>> s = 'acbed'
>>> sorted(s)
['a', 'b', 'c', 'd', 'e']
>>> ''.join(sorted(s))
'abcde'
```

## dict

### Keyがあるかないか

```py
D = {}
if s in D : # Dの中にsというキーがあるかどうか
  ...
else : 
```

### 辞書の値をすべて撮ってくる 

```py
D.values()
```

## complexity

> delやinsertはO(n)です。なので、基本使いません

> グローバルに書かずに、main()で囲む
```py
def main():
    """"ここに今までのコード"""

if __name__ == '__main__':
    main()
```

* [2019-06-14 Python 競技プログラミング高速化tips (PythonでAtcoderをやる際に個人的に気を付けてること)](https://juppy.hatenablog.com/entry/2019/06/14/Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E9%AB%98%E9%80%9F%E5%8C%96tips_%28Python%E3%81%A7Atcoder%E3%82%92%E3%82%84%E3%82%8B%E9%9A%9B%E3%81%AB%E5%80%8B)
* [2018-04-24 Pythonを高速にするTips集](https://cafeunder.github.io/rosenblock-chainers-blog/2018/04/24/Python-Tips.html)

## itertools

### accumulate - 累積和

```py
>>> list(itertools.accumulate([1,2,3,4]))
[1, 3, 6, 10]
```

### combinations - 組み合わせ

#### 組み合わせパターンを得る
```py
>>> list(itertools.combinations([1,2,3],2))
[(1, 2), (1, 3), (2, 3)]
```

#### 組み合わせ数が何個あるかを得る


```py
# これで良いらしい
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

>>> nCr(4,2)
```

古いやつ
```py
# nCr で nがめちゃくちゃでかい数の場合が多いので、以下を使うらしい
# 参考 : http://nemupm.hatenablog.com/entry/2015/01/03/234840
def modc(a, b, m):
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1, m) % m
    return c

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

>>> modc(6, 2, 2 ** 63 - 1)
15
```

## numpy

### np.argmax - 最大値の場所

```py
MAI = np.argmax(np.array(A))
```

## Tips

* プログラムを終了させるとき ```sys.exit()```

