from enum import Enum


def apoint(al):
    """
    algorithm to find articulation points in a graph.
    An articulation point v in a graph G is a point
    s.t. if v is removed from G then G will become
    disconnected.
    """

    Node = Enum("node", "UNVISITED, VISITED")
    # keeps track of which node was visited in what order
    dfs_num = [v for v in range(len(al))]
    # this ds holds the lowest df_count of a node v
    # that a node u can reach
    dfs_low = [v for v in range(len(al))]
    # keep track of the parent to remove bi-directional edges
    dfs_parent = [v for v in range(len(al))]
    # keep track of when a node is visited
    state = [Node.UNVISITED for _ in range(len(al))]
    # keep track of which nodes are articulation points
    art_point = [False for _ in range(len(al))]
    # number that tracks which order nodes are visited in
    dfs_count = 0

    def dfs(u):
        # dfs_count is an ordering of when vertices are visited
        nonlocal dfs_count
        # update vertex u state to visited
        state[u] = Node.VISITED
        # set dfs_low and dfs_num to dfs_count value
        dfs_low[u] = dfs_num[u] = dfs_count
        dfs_count += 1
        # iterate over neighbor vertices
        for v in al[u]:
            if state[v] == Node.UNVISITED:
                # set parent of neighbor vertex v to u
                dfs_parent[v] = u
                # handle edge case where the root has multiple children
                # and is therefore an articulation point if there is
                # more than 1 child
                if u == dfs_root:
                    nonlocal root_children
                    root_children += 1
                dfs(v)
                # after returning from recursive calls to all v neighbors of u
                # if v has not encountered an "ancestor" of u i
                # (by which dfs_num[v] will be lower than dfs_low[u])
                # then removing u will disconnect the graph.
                if dfs_low[v] >= dfs_num[u]:
                    art_point[u] = True
                # if a path through has found an ancestor of u and returned
                # then you can update dfs_low[u] to reflect the lower value
                dfs_low[u] = min(dfs_low[u], dfs_low[v])
            # for a vert u with neighbor v where v has been visited
            # and v is not the parent of u, (a bi-directional ege)
            # we update u with the low of v as it has reached an ancestor of its parent
            elif v != dfs_parent[u]:
                dfs_low[u] = min(dfs_low[u], dfs_num[v])

    for u, status in enumerate(state):
        if status == Node.UNVISITED:
            dfs_root = u
            root_children = 0
            dfs(u)
            art_point[u] = root_children > 1
    return art_point


if __name__ == "__main__":
    al = [[1], [2, 4], [], [4], [3, 5], [4]]
    res = apoint(al)
    ans = [False, True, False, False, True, False]
    assert res == ans

    al2 = [[1], [0, 2, 3, 4, 5], [1], [1], [1, 5], [1, 4]]
    res2 = apoint(al2)
    ans2 = [False, True, False, False, False, False]
    assert res2 == ans2
