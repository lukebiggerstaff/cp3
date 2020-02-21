from enum import Enum


def scc(al):
    """
    finds strongly connected components in a directed graph.
    a strongly connected component is a component s.t. for any
    u, v there is a path from u to v and v to u.
    """
    Node = Enum("node", "UNVISITED, VISITED")
    dfs_num = [v for v in range(len(al))]
    # ds to keep track of the low number found at vert
    # for cycle detection
    dfs_low = [v for v in range(len(al))]
    visited = [Node.UNVISITED for _ in range(len(al))]
    dfs_counter = 0
    scc_counter = 1
    stack = list()

    def dfs(u):
        nonlocal dfs_counter
        nonlocal scc_counter
        # upon initial visit to vertex set dfs_num and dfs_low
        # current dfs_counter
        dfs_low[u] = dfs_num[u] = dfs_counter
        dfs_counter += 1
        stack.append(u)
        visited[u] = Node.VISITED
        for v in al[u]:
            if visited[v] == Node.UNVISITED:
                dfs(v)
            if visited[v] == Node.VISITED:
                dfs_low[u] = min(dfs_low[u], dfs_low[v])

        # this node is the first node in this current
        # strongly connected component
        if dfs_low[u] == dfs_num[u]:
            print(f"SCC {scc_counter}")
            scc_counter += 1
            while True:
                v = stack.pop()
                print(f" {v}", end="")
                if u == v:
                    break
            print()

    for u, status in enumerate(visited):
        if status == Node.UNVISITED:
            dfs(u)


if __name__ == "__main__":
    al = [[1], [3], [1], [2, 4], [5], [7], [4], [6]]
    scc(al)
