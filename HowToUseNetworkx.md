# networkxの使い方
## はじめに

networkxはpythonでグラフを扱うためのライブラリです。
グラフの定義から、図示、探索などの操作が可能です。
ここでは、基本的な使い方を紹介します。
公式HPは[https://networkx.org/](https://networkx.org/)です。

## 準備
インストールは通常の方法ですから、省略します。
pythonコードの最初の部分で、ライブラリをインポートします。
`Point`は、座標を表すクラスです。
```python
import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
```

## グラフの定義
グラフは、頂点(node, vertex)と辺(edge)の集合で表現されます。
ここでは、辺に向きがある有向グラフを定義します。
頂点の位置`nodeLocations`は、作図の際に使います。
```python
# 頂点の定義
nodeList: list[str] = ["v0", "v1", "v2", "v3"]
# 頂点の位置座標
nodeLocations: dict[str, Point] = {
    "v0": Point(0.2, 0.2),
    "v1": Point(0.8, 0.2),
    "v2": Point(0.8, 0.8),
    "v3": Point(0.2, 0.8),
}
# 弧の定義
edgeList: list[tuple[str, str]] = [
    ("v0", "v1"),
    ("v0", "v3"),
    ("v1", "v2"),
    ("v2", "v3"),
    ("v3", "v1"),
]

G = nx.DiGraph()  # 有向グラフを定義
G.add_nodes_from(nodeList)  # 頂点を定義
G.add_edges_from(edgeList)  # 辺を定義
```

## グラフの描画
グラフを描画するには、matplotlibを使います。
```python
fig,ax=plt.subplots()
nx.draw(G, pos=nodeLocations, with_labels=True, node_size=1000, node_color="c", ax=ax)
plt.show()
```
このコードは[SimplestDiGraph.py](./SimplestDiGraph.py)にあります。`nx.draw()`には、作図のためのパラメータがたくさんあります。詳しくは、[公式HP](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html)を参照してください。
また、辺にラベルを付けるには、`nx.draw_networkx_edge_labels()`を使います。