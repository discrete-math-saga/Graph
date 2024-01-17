import networkx as nx
from enumerateCircuits import enumerateHamilton, drawGraph, Point


def defineGraph() -> tuple[nx.Graph, dict[str, Point], dict[tuple[str, str], str]]:
    """
    グラフの定義

    Returns
    ---
    G,nodeLocations,edgeLabels

    G nx.Graph グラフ
    nodeLocations 頂点の一覧
    edgeLabels 辺のラベル
    """
    nodeList: list[str] = list()
    for i in range(5):
        nodeList.append(f"v{i}")
    edgeList: list[tuple[str, str]] = [
        ("v0", "v1"),
        ("v0", "v2"),
        ("v0", "v3"),
        ("v0", "v4"),
        ("v1", "v2"),
        ("v1", "v3"),
        ("v2", "v4"),
        ("v3", "v4"),
    ]
    nodeLocations: dict[str, Point] = {
        "v0": Point(0.4, 0.8),
        "v1": Point(0.2, 0.6),
        "v2": Point(0.6, 0.6),
        "v3": Point(0.3, 0.4),
        "v4": Point(0.5, 0.4),
    }
    edgeLabels: dict[tuple[str, str], str] = dict()
    count = 0
    for e in edgeList:
        edgeLabels[e] = f"e{count}"
        count += 1
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G, nodeLocations, edgeLabels


if __name__ == "__main__":
    G, nodeLocations, edgeLabels = defineGraph()
    # drawGraph(G,nodeLocations,edgeLabels)
    result = enumerateHamilton("v0", G)
    print(len(result))
    for arcs in result:
        print(arcs)
