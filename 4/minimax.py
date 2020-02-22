class Node:
    def __init__(self, val):
        self.val = val
        self.leader = val
        self.rank = 1


class UF:
    def __init__(self, nodelist):
        self.storage = {key: Node(key) for key in nodelist}

    def find(self, key):
        node = self.storage[key]
        if node.leader == node.val:
            return node
        return self.find(node.leader)

    def union(self, n1, n2):
        l1 = self.find(n1)
        l2 = self.find(n2)
        if l1.rank == l2.rank:
            l2.leader = l1.val
            l1.rank += 1
        elif l1.rank > l2.rank:
            l2.leader = l1.val
        else:
            l1.leader = l2.val

    def same_set(self, n1, n2):
        return self.find(n1) == self.find(n2)


def minimax_path(el, i, j):
    """algorithm to find the minimum maximum edge weight path
    on a graph el, from vertex i to j
    """

    def path_find(u, j, al, path_value=0, visited=set()):
        visited.add(u)
        # update max value if we have reached destination
        if u == j:
            nonlocal max_value
            max_value = path_value
        for v, weight in al[u]:
            if v not in visited:
                # pass down current max value and recurse
                path_find(v, j, al, max(path_value, weight))

    # sort edge list in place to prepare for kruskal's algorithm
    # to construct the mst
    el.sort(key=lambda tup: tup[2])
    # add all nodes to set n to create the union-find ds
    n = set()
    for u, v, _ in el:
        n.update([u, v])
    al = [[] for _ in range(len(n))]
    ufds = UF(range(len(n)))
    for u, v, weight in el:
        if not ufds.same_set(u, v):
            # create adjacency list representation of MST
            al[u].append((v, weight))
            al[v].append((u, weight))
            ufds.union(u, v)
    max_value = 0
    path_find(i, j, al)
    return max_value


if __name__ == "__main__":
    el = [
        (0, 1, 50),
        (0, 2, 60),
        (1, 0, 50),
        (1, 3, 120),
        (1, 4, 90),
        (2, 0, 60),
        (2, 5, 50),
        (3, 1, 120),
        (3, 6, 70),
        (3, 5, 80),
        (4, 1, 90),
        (4, 6, 40),
        (5, 2, 50),
        (5, 3, 80),
        (5, 6, 140),
        (6, 3, 70),
        (6, 4, 40),
        (6, 5, 80),
    ]
    res = minimax_path(el, 1, 4)
    assert res == 80

    res2 = minimax_path(el, 5, 0)
    assert res2 == 60

    res3 = minimax_path(el, 6, 5)
    assert res3 == 80

    res4 = minimax_path(el, 5, 6)
    assert res4 == 80
