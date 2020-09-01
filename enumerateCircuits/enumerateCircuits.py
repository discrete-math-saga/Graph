import networkx as nx

def enumerateEuler(start,G):
    AEuler = list()
    circuits = list()
    enumerateEulerSub(start,start,AEuler,G,circuits)
    return circuits

def enumerateEulerSub(currentNode,startNode,AEuler,G, circuits):
    if (currentNode is startNode) and (len(G.edges) == len(AEuler)):
        circuits.append(AEuler)
        return
    for edge in nx.edges(G,currentNode):
        (f,t) = edge
        if (edge not in AEuler) and ((t,f) not in AEuler):
            A = list(AEuler)
            A.append(edge)
            (f,t) = edge
            enumerateEulerSub(t,startNode,A,G, circuits)

def enumerateHamilton(start,G):
    VHamilton = list()
    VHamilton.append(start)
    circuits = list()
    enumerateHamiltonSub(start,start,VHamilton,G,circuits)
    return circuits

def enumerateHamiltonSub(currentNode,startNode,VHamilton,G, circuits):
    for edge in nx.edges(G,currentNode):
        (f,t) = edge
        if (t is startNode) and (len(G.nodes) == len(VHamilton)):
            circuits.append(VHamilton)
        else:
            if t not in VHamilton:
                E = list(VHamilton)
                E.append(t)
                enumerateHamiltonSub(t,startNode,E,G,circuits)
