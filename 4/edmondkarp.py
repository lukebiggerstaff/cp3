from collections import deque
from queue import Queue


def edmondkarp(am, s, t):
    n = len(am)
    max_flow = 0
    res = [[0 for _ in range(n)] for _ in range(n)]

    def find_path(parent, i, path=None):
        if path is None:
            path = deque()
        if i == s:
            return path
        path.appendleft((parent[i], i))
        return find_path(parent, parent[i], path)

    def bfs():
        visited = [0 for _ in range(n)]
        parent = [v for v in range(n)]
        queue = Queue(maxsize=0)
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            visited[u] = 1
            for v, cap in enumerate(am[u]):
                if visited[v] == 0 and (cap - res[u][v]) > 0:
                    parent[v] = u
                    if v == t:
                        return find_path(parent, v)
                    queue.put(v)
        return []

    path = bfs()
    while len(path) > 0:
        flow = min(am[u][v] - res[u][v] for u, v in path)
        max_flow += flow
        for u, v in path:
            res[u][v] += flow
            res[v][u] -= flow
        path = bfs()
    return max_flow


if __name__ == "__main__":
    am = [[0, 0, 70, 30], [0, 0, 0, 0], [0, 25, 0, 5], [0, 70, 0, 0]]
    res = edmondkarp(am, 0, 1)
    assert res == 60
