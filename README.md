# AtCoder
AtCoder : https://atcoder.jp/

## How to start
* ABCに参加する
* [AtCoder に登録したら次にやること ～ これだけ解けば十分闘える！過去問精選 10 問 ～](https://qiita.com/drken/items/fd4e5e3630d0f5859067#5-%E9%81%8E%E5%8E%BB%E5%95%8F%E7%B2%BE%E9%81%B8-10-%E5%95%8F)
* 人のコードを読む
* [AtCoder Problems](https://kenkoooo.com/atcoder/) で過去問を解く

## Reference
* [2018-09-14 Python3で競技プログラミングする時に知っておきたいtips（入力編）](https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c)
* [2018-03-18 AtCoderで水色になるまでにやった事とかをまとめる](http://shibh308.hatenablog.com/entry/2018/03/18/074745)
    * Cまでは30分以内で解くのをいい目標感
    * Dを解くための武器を増やしていく

## Tips
* [docs/](docs/README.md)

## Learned 
* [尺取り法(Notebook)](notebook/ex_shakutori.ipynb) 
* 累積和
* MODでの四則演算
   * 足し算 : 先にしようが後からしようが同じ結果
   * かけ算 : aとbで先にしてからmodを取るのと、後からしてからmodを取るのは同じ結果
   * 参考 : [modにおける四則演算](https://ttrsq.exblog.jp/24409121/) 
* 動的計画法（DP）
    * 今の状態が次の状態に影響するような問題
* [ダイクストラ法(Notebook)](ex_dijkstra.ipynb)
* [Union Find Tree(Notebook)](ex_union_find_tree.ipynb)
* Depth First Search / Breadth First Search
* [二分探索(Notebook)](ex_bisect.ipynb)

## Problem pattern
* X回の操作で、最大で何個にできるでしょうか (ABC140 D)
    * 一回の操作で増やせる数が実は決まってることがある
    * 増やせる候補に着目して、問題をシンプル化することが大事

## Next step
* 桁DP 
