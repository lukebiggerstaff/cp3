from collections import deque


def create_adj(n, edges):
    """create adjlist from n vertices and list of edges"""
    adj = []
    for row in edges:
        adj.append(row)  # append each edge to the start vertex
    return adj


def count(adj):
    """count number of vertices and edges in graph"""
    n = len(adj)
    e = 0
    for row in adj:
        e += len(row)
    return n, e


def inoutdeg(adj, v):  # count in and out degree of a certain vertex v
    """count in and out degree of a certain vertex v from an adjacency list adj"""
    if v > len(adj) - 1:
        return None
    indeg = 0
    outdeg = len(adj[v])
    for edges in adj:
        if v in edges:
            indeg += 1
    return indeg, outdeg


def tpose(adj):
    """transpose adjacency list adj and return new list t"""
    n = len(adj)
    t = [[] for _ in range(n)]
    for i in range(n):
        for j in adj[i]:
            t[j].append(i)
    return t


def is_complete(adj):
    """check if adjacency list adj is a complete graph"""
    n = len(adj)
    v = set(list(range(n)))
    for i in range(n):
        edges = set()
        for dest in adj[i]:
            if dest == i:
                continue
            edges.add(dest)
        if edges != (v - set([i])):
            return False
    return True


def is_tree(adj):
    """check if adjancency list adj is a tree"""
    edges = set()
    visited = set()
    q = deque([0])
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        for dest in adj[curr]:
            edges.add((min(curr, dest), max(curr, dest)))
            q.append(dest)
        visited.add(curr)
    if len(visited) != len(adj):
        return False
    if len(edges) > len(adj):
        return False
    return True


def is_star(adj):
    """check if adjacency list adj is a star graph
        1. one node has degree v - 1
        2. all nodes except central node have degree 1
        3. number of edges is equal to number of vertices - 1
    """
    n = len(adj)
    visited = set()
    q = deque([0])
    totedges = set()
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        numedges = len(adj[curr])
        if not (numedges == 1 or numedges == n - 1):
            return False
        for dest in adj[curr]:
            q.append(dest)
            totedges.add((min(curr, dest), max(curr, dest)))
        visited.add(curr)
    if len(visited) < n:
        return False
    if len(edges) >= n:
        return False
    return True


if __name__ == "__main__":
    n = 3
    edges = [[1, 2], [2, 0], [1, 0]]
    adj = create_adj(n, edges)

    numv, nume = count(adj)
    assert numv == 3
    assert nume == 6

    indeg, outdeg = inoutdeg(adj, 0)
    assert indeg == 2
    assert outdeg == 2

    n = 3
    edges = [[2], [2, 0], [1, 0]]
    adj = create_adj(n, edges)
    t = tpose(adj)

    # check t is transpose of adj
    for i in range(n):
        for j in adj[i]:
            assert i in t[j]

    # check adj is transpose of t
    for i in range(n):
        for j in t[i]:
            assert i in adj[j]

    c_graph = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    assert is_complete(c_graph) == True

    tree = [[2, 3], [6], [0, 4, 5], [0, 7, 8], [2], [2, 6], [1, 5], [3], [3]]
    not_tree = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    assert is_tree(tree) == True
    assert is_tree(not_tree) != True

    star = [[1, 2, 3], [0], [0], [0]]
    not_star = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    assert is_star(star) == True
    assert is_star(not_star) != True
