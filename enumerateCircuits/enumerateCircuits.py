import networkx as nx

def enumerateEuler(start:str, G:nx.Graph) -> list[list[str]]:
    """
    Euler閉路を列挙する

    Parameters
    ---
    start 探索を開始する頂点

    G 対象となる無向グラフ

    Returns
    ---
    Euler閉路を構成する辺のリストのリスト
    """
    AEuler = list()
    circuits = list()
    _enumerateEulerSub(start, start, AEuler, G, circuits)
    return circuits

def _enumerateEulerSub(currentNode:str, startNode:str, AEuler:list[tuple[str,str]], G:nx.Graph, circuits:list[list[str]]):
    """
    Euler閉路を列挙する再帰メソッド

    Parameters
    ---
    currentNode 現在の頂点

    startNode 探索の始点
    
    ACuler 探索中の閉路に属する辺のリスト
    
    G 対象となるグラフ
    
    circuits 発見した閉路のリスト
    """

    if (currentNode is startNode) and (len(G.edges) == len(AEuler)):
        circuits.append(AEuler)
        return
    for edge in nx.edges(G,currentNode):
        (f,t) = edge
        if (edge not in AEuler) and ((t,f) not in AEuler):
            A = list(AEuler)
            A.append(edge)
            (f, t) = edge
            _enumerateEulerSub(t, startNode, A, G, circuits)

def enumerateHamilton(start:str, G:nx.Graph) -> list[list[str]]:
    """
    Hamilton閉路を列挙する

    ---
    start 探索を開始する頂点

    G 対象となる無向グラフ

    Returns
    ---
    Hamilton閉路を構成する頂点のリストのリスト
    """
    VHamilton = list()
    VHamilton.append(start)
    circuits = list()
    _enumerateHamiltonSub(start, start, VHamilton, G, circuits)
    return circuits

def _enumerateHamiltonSub(currentNode:str, startNode:str, VHamilton:list[str], G:nx.Graph, circuits:list[list[str]]):
    """
    Hamilton閉路を列挙する再帰メソッド

    Parameters
    ---
    currentNode 現在の頂点

    startNode 探索の始点
    
    VHamilton 探索中の閉路に属する頂点のリスト
    
    G 対象となるグラフ
    
    circuits 発見した閉路のリスト
    """
    for edge in nx.edges(G, currentNode):
        (f, t) = edge
        if (t is startNode) and (len(G.nodes) == len(VHamilton)):
            circuits.append(VHamilton)
        else:
            if t not in VHamilton:
                E = list(VHamilton)
                E.append(t)
                _enumerateHamiltonSub(t, startNode, E,G, circuits)
