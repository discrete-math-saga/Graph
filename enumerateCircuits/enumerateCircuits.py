import networkx as nx
import matplotlib.pyplot as plt
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def enumerateEuler(start: str, G: nx.Graph) -> list[list[tuple[str, str]]]:
    """
    Enumerate Euler circuits

    Parameters
    ---
    start: The starting node for the search
    G: The target graph

    Returns
    ---
    The list of lists containing edges forming an Euler circuit
    """
    circuitEuler: list[tuple[str, str]] = list()  # An Euler circuit as list of edges
    circuits: list[list[tuple[str, str]]] = list()  # lists of Euler circuits
    _enumerateEulerSub(start, start, circuitEuler, G, circuits)
    return circuits


def _enumerateEulerSub(
    currentNode: str,
    startNode: str,
    circuitEuler: list[tuple[str, str]],
    G: nx.Graph,
    circuits: list[list[tuple[str, str]]],
):
    """
    The recursive methods for enumerating Euler circuits

    Parameters
    ---
    currentNode
    startNode: The starting node for the search
    circuitEuler: The list of edges for the current search process
    G: The target graph
    circuits: The list of circuits found
    """

    if (currentNode is startNode) and (len(G.edges) == len(circuitEuler)):
        circuits.append(circuitEuler)
        return
    for edge in nx.edges(G, currentNode):
        f: str
        t: str
        (f, t) = edge
        if (edge not in circuitEuler) and ((t, f) not in circuitEuler):
            A = list(circuitEuler)
            A.append(edge)
            _enumerateEulerSub(t, startNode, A, G, circuits)


def enumerateHamilton(start: str, G: nx.Graph) -> list[list[str]]:
    """
    Enumerate Hamilton circuits

    Parameters
    ---
    start: The starting node for the search
    G: The target graph

    Returns
    ---
    The list of lists containing nodes forming a Hamilton circuit
    """
    circuitHamilton: list[str] = list()
    circuitHamilton.append(start)
    circuits: list[list[str]] = list()
    _enumerateHamiltonSub(start, start, circuitHamilton, G, circuits)
    return circuits


def _enumerateHamiltonSub(
    currentNode: str,
    startNode: str,
    circuitHamilton: list[str],
    G: nx.Graph,
    circuits: list[list[str]],
):
    """
    The recursive methods for enumerating Hamilton circuits

    Parameters
    ---
    currentNode
    startNode:The starting node for the search

    circuitHamilton: The list of nodes for the current search process
    G: The target graph
    circuits: The list of circuits found
    """
    for edge in nx.edges(G, currentNode):
        f: str
        t: str
        (f, t) = edge
        if (t is startNode) and (len(G.nodes) == len(circuitHamilton)):
            circuits.append(circuitHamilton)
        else:
            if t not in circuitHamilton:
                E = list(circuitHamilton)
                E.append(t)
                _enumerateHamiltonSub(t, startNode, E, G, circuits)


def enumerateEulerNonRecursive(
    start: str, G: nx.Graph
) -> list[list[tuple[str | None, str]]]:
    """
    Non-recursive method for enumerating Euler circuits

    Parameters
    ---
    start: The starting node for searching
    G: The target graph

    Returns
    ---
    The list of lists containing edges forming an Euler circuit

    """
    # THe list of lists containing edges
    circuits: list[list[tuple[str | None, str]]] = list()  
    # A stack for waiting searches
    stack: list[tuple[str, list[tuple[str | None, str]]]] = [(start, [(None, start)])]
    n: int = len(G.edges())  # The number of edges
    while len(stack) > 0:
        # Popping the next candidate for searching
        # v: the current nodes
        # A: the list of edges expressing the path
        v: str
        edgeList: list[tuple[str | None, str]]
        v, edgeList = stack.pop(-1)
        if len(edgeList) > 0:
            # the last element (the previous) of the edges
            e: tuple[str | None, str] = edgeList[-1]  
            if e[0] is None:
                e = edgeList.pop(-1)
            if (v == start and len(edgeList) == n):  # If the circuit reaches the starting node
                circuits.append(edgeList)
            elif len(edgeList) < n:
                for w in G.neighbors(v):
                    #  The edges is not the used previously
                    if (v, w) in edgeList or (w, v) in edgeList:
                        continue
                    else:
                        edgeListCopy: list[tuple[str | None, str]] = edgeList.copy()
                        edgeListCopy.append((v, w))
                        stack.append((w, edgeListCopy))
    return circuits


def enumerateHamiltonNonRecursive(start: str, G: nx.Graph) -> list[list[str]]:
    """
    Enumerate Hamilton circuits non-recursively

    Parameters
    ---
    start: the starting node for searching
    G: the target graph

    Returns
    ---
    The list of lists containing nodes forming a Hamilton circuit

    """
    circuits: list[list[str]] = list()
    stack: list[list[str]] = [[start]]
    n = len(G.nodes())
    while len(stack) > 0:
        edgeList: list[str] = stack.pop(-1)
        v = edgeList[-1]
        if v == start and len(edgeList) == n + 1:
            circuits.append(edgeList)
        elif len(edgeList) <= n:
            for w in G.neighbors(v):
                if w == start or w not in edgeList:
                    edgeListCopy = edgeList.copy()
                    edgeListCopy.append(w)
                    stack.append(edgeListCopy)
    return circuits


def drawGraph(
    G: nx.Graph,
    nodeLocations: dict[str, Point],
    edgeLabels: dict[tuple[str, str], str],
    font_size=12,
    node_size=1000,
    edge_width=2.0,
    node_color="c",
) -> None:
    """
    Drawing graphs
    """
    fig,ax=plt.subplots(facecolor="white")

    # nx.draw_networkx_nodes(G, nodeLocations, node_size=node_size, node_color=node_color,ax=ax)
    # nx.draw_networkx_labels(G, nodeLocations, font_size=font_size,ax=ax)
    # nx.draw_networkx_edges(
    #     G, nodeLocations, width=edge_width, arrows=False, node_size=node_size,ax=ax
    # )
    nx.draw(G, nodeLocations, with_labels=True, node_size=node_size, node_color=node_color,width=edge_width,ax=ax)
    nx.draw_networkx_edge_labels(
        G, nodeLocations, edge_labels=edgeLabels, font_size=font_size,ax=ax
    )
    ax.axis("off")
    plt.show()
