def dominator(al, x, y):
    """find if vertex Y is dominated by vertex X
    """

    visited = set()
    y_reachable = False

    def dfs(i):
        if i == y:
            nonlocal y_reachable
            y_reachable = True
        if i != x:
            for nxt in al[i]:
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt)

    dfs(0)
    return not y_reachable


if __name__ == "__main__":
    al2 = [[1, 2], [3], [3], [4], []]
    res = dominator(al2, 3, 4)
    assert res == True

    res2 = dominator(al2, 4, 3)
    assert res2 == False
