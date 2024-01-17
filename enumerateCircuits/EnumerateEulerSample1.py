import networkx as nx
from enumerateCircuits import enumerateEuler, drawGraph, Point


def defineGraph() -> tuple[nx.Graph, dict[str, Point], dict[tuple[str, str], str]]:
    """
    Defining the target graph

    Returns
    ---
    G,nodeLocations,edgeLabels

    G: the graph
    nodeLocations: the list of nodes
    edgeLabels: the list of edge labels
    """
    nodeList: list[str] = list()
    for i in range(5):
        nodeList.append(f"v{i}")
    edgeList: list[tuple[str, str]] = [
        ("v0", "v1"),
        ("v0", "v2"),
        ("v1", "v2"),
        ("v1", "v3"),
        ("v1", "v4"),
        ("v2", "v3"),
        ("v2", "v4"),
    ]
    nodeLocations: dict[str, Point] = {
        "v0": Point(0.4, 0.8),
        "v1": Point(0.2, 0.6),
        "v2": Point(0.6, 0.6),
        "v3": Point(0.2, 0.4),
        "v4": Point(0.6, 0.4),
    }
    edgeLabels: dict[tuple[str, str], str] = dict()
    c = 0
    for e in edgeList:
        edgeLabels[e] = f"e{c}"
        c += 1
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    return G, nodeLocations, edgeLabels


if __name__ == "__main__":
    G, nodeLocations, edgeLabels = defineGraph()
    drawGraph(G, nodeLocations, edgeLabels)
    result: list[list[tuple[str, str]]] = enumerateEuler("v0", G)
    print(len(result))
    for arcs in result:
        route = list()
        for a in arcs:
            e: tuple[str, str] = a
            if e not in edgeLabels:
                f: str
                t: str
                (f, t) = e
                e = (t, f)
            route.append(edgeLabels[e])
        print(route)
