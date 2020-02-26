from math import inf
from collections import deque


def is_bipartite(al):
    """
    This algorithm determines if a graph is bipartite by traversing 
    breadth-first and coloring each node one of two colors, current node
    is one color and all its neighbors are another. If a node finds 
    an already colored/visited node and it is not the opposite color
    then we know that the graph is not bipartite.
    """
    colors = [inf for _ in range(len(al))]

    # color first point 0
    colors[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        u_color = colors[u]
        for v in al[u]:
            # color node if it is not already colored
            if colors[v] == inf:
                queue.append(v)
                colors[v] = 1 - u_color
            # if color matches current node color
            # than graph is not bipartite.
            if colors[v] == u_color:
                return False
    return True


if __name__ == "__main__":
    bipartite_al = [[1, 3], [0, 2], [1, 3], [0, 2]]
    res = is_bipartite(bipartite_al)
    assert res == True

    not_bipartite_al = [[1, 2, 3], [0, 2], [1, 3], [0, 2]]
    res2 = is_bipartite(not_bipartite_al)
    assert res2 == False

