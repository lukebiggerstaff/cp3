from queue import Queue


def edmondkarp(am, s, t):
    n = len(am)
    max_flow = 0

    def find_path():
        visited = [0 for _ in range(n)]
        parent = [v for v in range(n)]
        queue = Queue(maxsize=0)
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            visited[u] = 1
            for v, cap in enumerate(am[u]):
                if visited[v] == 0 and cap > 0:
                    parent[v] = u
                    if v == t:
                        return parent
                    queue.put(v)
        return []

    path = find_path()


if __name__ == "__main__":
    am = [[0, 0, 70, 30], [0, 0, 0, 0], [0, 25, 0, 5], [0, 70, 0, 0]]
    res = edmondkarp(am, 0, 1)
    print(res)
