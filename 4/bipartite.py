from collections import deque


def is_bipartite(al):
    """
    algorithm to determine if a graph is bipartite.
    """
    visited = [0 for _ in range(len(al))]
    color = [(1 << 20) for _ in range(len(al))]

    color[0] = 0
    queue = deque([0])
    while queue:
        i = queue.popleft()
        i_color = color[i]
        visited[i] = 1
        for j in al[i]:
            if color[j] == (1 << 20):
                queue.append(j)
                color[j] = 1 - i_color
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

