import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def position2xy(
    nodeLocations: dict[str, Point]
) -> tuple[dict[str, float], dict[str, float]]:
    """
    位置の一覧から、X座標とY座標の一覧を生成

    Parameters
    ---
    nodeLocations 頂点名->座標の一覧

    Returns
    ---
    (xp,yp) 頂点名->X座標の一覧、頂点名->Y座標の一覧
    """
    xp:dict[str,float] = dict()
    yp:dict[str,float] = dict()
    for v in nodeLocations.keys():
        xp[v] = nodeLocations[v].x
        yp[v] = nodeLocations[v].y
    return xp, yp


def defineGraph() -> tuple[nx.DiGraph, dict[str, Point], dict[tuple[str, str], str]]:
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
    # 弧のラベル
    edgeLabels = dict()
    c = 0
    for e in edgeList:
        edgeLabels[e] = f"e{c}"
        c += 1

    G = nx.DiGraph()  # 有向グラフを定義
    G.add_nodes_from(nodeList)  # 頂点を定義
    G.add_edges_from(edgeList)  # 辺を定義
    xp:dict[str,float]
    yp:dict[str,float]    
    xp, yp = position2xy(nodeLocations)
    nx.set_node_attributes(G, xp, "x")  # 頂点のX座標
    nx.set_node_attributes(G, yp, "y")  # 頂点のY座標
    nx.set_edge_attributes(G, edgeLabels, "edge")  # 辺の定義
    return G, nodeLocations, edgeLabels


def drawGraph(
    G: nx.DiGraph,
    nodeLocations: dict[str, Point],
    edgeLabels: dict[tuple[str, str], str],
) -> None:
    """
    作図
    """
    # 準備
    font_size = 24
    node_size = 5000
    edge_width = 5.0
    node_color = "c"
    arrowsize = 50
    fig,ax = plt.subplots(figsize=(10, 10), facecolor="white")

    # 頂点を描く
    nx.draw_networkx_nodes(G, nodeLocations, node_size=node_size, node_color=node_color,ax=ax)
    nx.draw_networkx_labels(G, nodeLocations, font_size=font_size,ax=ax)
    nx.draw_networkx_edges(
        G,
        nodeLocations,
        width=edge_width,
        arrows=True,
        arrowsize=arrowsize,
        node_size=node_size,
        ax=ax
    )
    # 辺を描く
    nx.draw_networkx_edge_labels(
        G, nodeLocations, edge_labels=edgeLabels, font_size=font_size,ax=ax
    )
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    G, nodeLocations, edgeLabels = defineGraph()
    drawGraph(G, nodeLocations, edgeLabels)
    nx.write_pajek(G, "sampleDiGraph.net")
    G.edges(data=True)
