from collections import deque


def create_elist(n, edges):
    elist = []
    for i in range(n):
        for j in edges[i]:
            elist.append((i, j))  # append tuple for each edge
    return elist


def count(elist):
    """count number of vertices and edges in graph"""
    n = set()
    e = len(elist)
    for v, w in elist:
        n.update([v, w])
    return len(n), e


def inoutdeg(elist, v):  # count in and out degree of a certain vertex v
    """count in and out degree of a certain vertex v from an edge list elist"""
    indeg = 0
    outdeg = 0
    for a, b in elist:
        if v == a:
            outdeg += 1
        if v == b:
            indeg += 1
    return indeg, outdeg


def tpose(elist):
    """transpose edge list elist and return new list t"""
    t = list()
    for v, w in elist:
        t.append((w, v))
    return t


if __name__ == "__main__":
    n = 3
    edges = [[1, 2], [2, 0], [1, 0]]
    elist = create_elist(n, edges)

    numv, nume = count(elist)
    assert numv == 3
    assert nume == 6

    indeg, outdeg = inoutdeg(elist, 0)
    assert indeg == 2
    assert outdeg == 2

    n = 3
    edges = [[2], [2, 0], [1, 0]]
    elist = create_elist(n, edges)
    t = tpose(elist)

    # check t is transpose of elist
    for v, w in elist:
        assert (w, v) in t

    # check elist is transpose of t
    for v, w in t:
        assert (w, v) in elist
