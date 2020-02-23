from queue import Queue


def sssp(al, i, j):
    """
    algorithm to find the single source shortest path from i to j on
    an unweighted graph. This implementation uses a breadth-first
    search and then returns the path in the form of a stack.
    """
    # initializing queue to maxsize=0 means the
    # queue is unbounded and can grow as needed.
    q = Queue(maxsize=0)
    # initialize each node to be its own parent
    parent = [v for v in range(len(al))]
    visited = set()
    q.put(i)
    found = False
    while q and not found:
        u = q.get()
        visited.add(u)
        for v in al[u]:
            if v == j:
                parent[v] = u
                found = True
            if v not in visited:
                parent[v] = u
                q.put(v)

    stack = list([j])
    curr = j
    while curr != i:
        curr = parent[curr]
        stack.append(curr)
    return stack


if __name__ == "__main__":
    al = [[1], [2], [3], [4], []]
    s = sssp(al, 0, 4)
    assert s == [4, 3, 2, 1, 0]

    s1 = sssp(al, 1, 3)
    assert s1 == [3, 2, 1]
