import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

# グラフの定義
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

# 作図
fig,ax=plt.subplots()
nx.draw(G, pos=nodeLocations, with_labels=True, node_size=1000, node_color="c", ax=ax)
plt.show()
