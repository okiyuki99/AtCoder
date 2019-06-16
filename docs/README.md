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

