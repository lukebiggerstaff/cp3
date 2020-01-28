from collections import deque


def create_am(n, edges):
    """creates a directed adjacency matrix representation of a graph"""
    matrix = [[0 for _ in range(n)] for _ in range(n)]  # initialize matrix to size VxV
    for i in range(n):
        for j in edges[i]:
            matrix[i][j] = 1
    return matrix


def create_uam(n, edges):
    """creates an undirected graph as adjacency matrix"""
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1
            matrix[j][i] = 1
    return matrix


def count(am):
    """ count number of vertices and edges in graph"""
    n = len(am)
    e = 0
    for i in range(n):
        for j in range(n):
            if am[i][j] != 0:
                e += 1
    return n, e


def inoutdeg(am, v):  # count in and out degree of a certain vertex v
    """count in and out degree of a certain vertex v"""
    indeg = outdeg = 0
    if v > len(am) - 1:
        return None
    for i in am[v]:
        if i != 0:
            outdeg += 1
    for row in am:
        if row[v] != 0:
            indeg += 1
    return indeg, outdeg


def tpose(am):
    """transpose adjacency matrix and return new matrix t"""
    n = len(am)
    t = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = am[i][j]
    return t


def tpose2(am):
    """tranpose adjacency matrix in place"""
    n = len(am)
    for i in range(n):
        for j in range(n):
            temp = am[i][j]
            am[i][j] = am[j][i]
            am[j][i] = temp


def is_complete(am):
    """check if adjacency matrix am is a complete graph"""
    n = len(am)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            elif am[i][j] != 1:
                return False
    return True


def is_tree(am):
    """check if adjancency matrix am is a tree"""
    edges = set()
    visited = set()
    q = deque()
    q.append(0)
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        for i, dest in enumerate(am[curr]):
            if dest != 0:
                edges.add((min(curr, i), max(curr, i)))
                q.append(i)
        visited.add(curr)
    if len(visited) != len(am):
        return False
    if len(edges) > len(am):
        return False
    return True


def is_star(am):
    """check if adjancency matrix am is a star graph"""
    n = len(am)
    visited = set()
    q = deque()
    q.append(0)
    while q:
        curr = q.popleft()
        if curr in visited:
            continue
        total = 0
        for i in range(n):
            if am[curr][i] == 1:
                q.append(i)
                total += 1
        if not (total == 1 or total == n - 1):
            return False
        visited.add(curr)
    if len(visited) < len(am):
        return False
    return True


if __name__ == "__main__":
    n = 3
    edges = [[1, 2], [2, 0], [1, 0]]
    am = create_am(n, edges)

    numv, nume = count(am)
    assert numv == 3
    assert nume == 6

    indeg, outdeg = inoutdeg(am, 0)
    assert indeg == 2
    assert outdeg == 2

    n = 3
    edges = [[2], [2, 0], [1, 0]]
    am = create_am(n, edges)

    t = tpose(am)
    for i in range(n):
        for j in range(n):
            assert am[i][j] == t[j][i]

    c_graph = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    assert is_complete(c_graph) == True

    tree = [
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]
    not_tree = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert is_tree(tree) == True
    assert is_tree(not_tree) != True

    star = [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    not_star = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert is_star(star) == True
    assert is_star(not_star) != True
