from collections import deque


def tsort(al):
    """
    recursive topological sort algorithm
    """
    n = len(al)
    slist = deque()
    visited = [0 for v in range(n)]

    def dfs(i):
        visited[i] = 1
        for nxt in al[i]:
            if visited[nxt] == 0:
                dfs(nxt)
        slist.appendleft(i)

    for i in range(n):
        if visited[i] == 0:
            dfs(i)
    return slist


if __name__ == "__main__":
    al = [[1], [2], [3], [4], [5], []]
    ans = deque([0, 1, 2, 3, 4, 5])

    res = tsort(al)
    assert res == ans

    al2 = [[1, 2], [2, 3], [3, 5], [4], [], [], [], [6]]
    res2 = tsort(al2)
    ans2 = deque([7, 6, 0, 1, 2, 5, 3, 4])
    assert res2 == ans2
