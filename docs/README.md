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

# -1をかけたものを取得する
A = list(map(lambda x : int(x) * -1, input().split()))
```

### 複数行に渡る整数1つ入力をリストに

```py
# H  WW
# S1
# ...
# SH
H, W = map(int, input().split())
S = [input() for _ in range(H)]
```

### 複数行に渡る整数複数入力をリストに

```py
# N
# T1 T2
# T3 T4 T5
# ...
T = [list(map(int,input().split())) for _ in range(N)]
```

### 

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

### Basic

```py
>>> 321 % 100 # mod = 余り計算
21
>>> 321 // 100 # 商だけ
3
>>> 2 ** 3 # 乗
8
```

### 整数除算

```py
>>> 3 / 2
1.5
>>> 3 // 2 # 切り捨てになるよ
1
```

* abc139_d : 整数除算の//しないと浮動小数点の誤差でやられることがある

```py
>>> 10 ** 16 * (10 ** 16 - 1) // 2
49999999999999995000000000000000
>>> int(10 ** 16 * (10 ** 16 - 1) / 2)
49999999999999993675881847455744
```

* 32bit整数型に収まらないときの整数同士の割り算のときは // を使うほうが無難。

切り捨て分だけ本当の割り算結果よりは小さくなるけど、整数で返ってくるのを担保できる


### ビット演算子

```py
# 排他的論理和 ^ 
>>> True ^ False 
True
>>> True ^ True
False
```

### math module

```py
import math

print(math.ceil(7.5)) # -> 8 # 切り上げ
print(math.floor(7.5)) # -> 7 # 切り捨て

print(math.ceil(-7.5)) # -> -7
print(math.floor(-7.5)) # -> -8

print(math.trunc(7.5)) # -> 7 # 整数部分を取得
print(math.trunc(-7.5)) # -> -7
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

### ある文字が該当する文字列に入ってるかどうか

```py
'A' in 'ABC' # -> True
# これはだめ : A' in ['A,'B',C']
'A' in str(['A','B','C']) # -> True
```

### Alphabet の文字列を取得する

```py
ALPHA = [chr(ord('A') + i) for i in range(26)]
print(ALPHA)
>>> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

# ある数字のシーケンス
>>> list(range(5))
[0, 1, 2, 3, 4]
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

### 辞書の値をすべて取ってくる

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

abc137_c のように、nC2を求める場合、今何個あるかの情報を使えば、今ある個数分を足していけば、答えは得れる

```
1c2 0 
2c2 1
3c2 3
4c2 6
5c2 10

つまり、10 = 6 + 4
```

何も考えるに求める場合

```py
# これで良いらしい
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
import math

def nCr(n,r):
    f = math.factorial # 階乗（e.g., n!）を求める関数
    return f(n) // f(r) // f(n-r)

>>> nCr(4,2)
```

```py
# nCr で nがめちゃくちゃでかい数の場合が多いので、以下を使う。
# nCr mod mはmodc(n,r,m)で得られる。
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

### あるリストに同じ値を掛ける(multiply)はnumpyが速い

```py
>>> a = [1,2,3]
>>> list(np.array(a) * -3)
[-3, -6, -9]
```

## Tips

#### プログラムを終了させるとき ```sys.exit()```

#### True / False を 1 / 0 

``` py
>>> print([0,1][True])
1
>>> print([0,1][False])
0
```

## Learned
* **abc137_d**
    * 前向きに数えるよりも、後ろ向きに数えたほうがいいときがある
    * 追加、最大(小)値取り出しの繰り返しには `ヒープを用いた優先付きキュー`
