import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float

def defineGraph() -> tuple[nx.Graph, dict[str, Point], dict[tuple[str, str], str]]:
    """
    グラフの定義

    Returns
    ---
    G,nodeLocations,edgeLabels

    G nx.DiGraph グラフ
    nodeLocations 頂点の一覧
    edgeLabels 辺のラベル
    """
    # 頂点の定義
    nodeList: list[str] = ["v0", "v1", "v2", "v3", "v4"]
    # 頂点の位置座標
    nodeLocations: dict[str, Point] = {
        "v0": Point(0.2, 0.2),
        "v1": Point(0.8, 0.2),
        "v2": Point(0.5, 0.5),
        "v3": Point(0.8, 0.8),
        "v4": Point(0.2, 0.8),
    }
    # 弧の定義
    edgeList: list[tuple[str, str]] = [
        ("v0", "v1"),
        ("v0", "v2"),
        ("v0", "v4"),
        ("v1", "v2"),
        ("v1", "v3"),
        ("v2", "v3"),
        ("v2", "v4"),
    ]
    # 弧のラベル
    edgeLabels = dict()
    c = 0
    for e in edgeList:
        edgeLabels[e] = f"e{c}"
        c += 1

    G = nx.Graph()  # 無向グラフを定義
    G.add_nodes_from(nodeList)  # 頂点を定義
    G.add_edges_from(edgeList)  # 辺を定義
    nx.set_edge_attributes(G, edgeLabels, "edge")  # 辺の定義
    return G, nodeLocations, edgeLabels

def drawGraph(
    G: nx.Graph, nodeLocations: dict[str, Point], edgeLabels: dict[tuple[str, str], str]
) -> None:
    """
    作図
    """
    # 準備
    font_size = 24
    node_size = 5000
    edge_width = 5.0
    node_color = "c"
    arrow_size = 50
    fig,ax = plt.subplots(figsize=(10, 10), facecolor="white")

    nx.draw(G, nodeLocations, with_labels=True, node_size=node_size, node_color=node_color, font_size=font_size,width=edge_width,arrowsize=arrow_size,ax=ax)
    # 辺を描く
    nx.draw_networkx_edge_labels(
        G, nodeLocations, edge_labels=edgeLabels, font_size=font_size,ax=ax
    )
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    create = True
    G: nx.Graph
    if create:
        G, nodeLocations, edgeLabels = defineGraph()
        drawGraph(G, nodeLocations, edgeLabels)
        nx.write_pajek(G, "sampleGraph.net")
        G.edges(data=True)
    else:
        G = nx.read_pajek("sampleGraph.net")
        G.nodes(data=True)

    # 無向であることを確認
    nodes = list(nx.nodes(G))
    n = len(nodes)
    b1 = (nodes[0], nodes[1]) in nx.edges(G)
    b2 = (nodes[1], nodes[0]) in nx.edges(G)
    print(n, b1, b2)
