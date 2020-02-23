from collections import deque


def is_bipartite(al):
    """
    This algorithm determines if a graph is bipartite by traversing 
    breadth-first and coloring each node one of two colors, current node
    is one color and all its neighbors are another. If a node finds 
    an already colored/visited node and it is not the opposite color
    then we know that the graph is not bipartite.
    """
    color = [(1 << 20) for _ in range(len(al))]

    # color first point 0
    color[0] = 0
    queue = deque([0])
    while queue:
        i = queue.popleft()
        i_color = color[i]
        for j in al[i]:
            # color node if it is not already colored
            if color[j] == (1 << 20):
                queue.append(j)
                color[j] = 1 - i_color
            # if color matches current node color
            # than graph is not bipartite.
            if color[j] == i_color:
                return False
    return True


if __name__ == "__main__":
    bipartite_al = [[1, 3], [0, 2], [1, 3], [0, 2]]
    res = is_bipartite(bipartite_al)
    assert res == True

    not_bipartite_al = [[1, 2, 3], [0, 2], [1, 3], [0, 2]]
    res2 = is_bipartite(not_bipartite_al)
    assert res2 == False

