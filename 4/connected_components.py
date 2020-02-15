def connected_components(al):
    """find all connected components in a graph
    """

    n = len(al)
    vertices = [v for v in range(n)]
    unvisited = [0 for _ in range(n)]
    cc = 1

    def dfs(v):
        print(f"{v} ", end="")
        unvisited[v] = 1
        for nxt in al[v]:
            if unvisited[nxt] == 0:
                dfs(nxt)

    for vert in vertices:
        if unvisited[vert] == 0:
            print(f"cc {cc}: ", end="")
            cc += 1
            dfs(vert)
            print()


if __name__ == "__main__":
    al = [[1], [2], [0], [4, 5], [], [], [7, 8], [], [], []]
    connected_components(al)
