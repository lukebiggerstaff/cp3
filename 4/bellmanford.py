from math import inf


def bellmanford(al, s):
    """
    implementation of the bellman-ford algorithm to find
    the single source shortest path from s to every other
    vertex in a directed, weighted graph
    """
    dist = [inf for _ in range(len(al))]
    dist[s] = 0
    n = len(al)
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in al[u]:
                dist[v] = min(dist[v], dist[u] + weight)
    # check for negative cycle
    negative_cycle = False
    for u in range(n):
        for v, weight in al[u]:
            if dist[v] > dist[u] + weight:
                negative_cycle = True
    print(f"negative cycle = {negative_cycle}")
    return dist


if __name__ == "__main__":
    al = [[(4, 1)], [(3, 3), (4, 6)], [(1, 2), (0, 6), (3, 7)], [(4, 5)], []]
    res = bellmanford(al, 2)
    assert res == [6, 2, 0, 5, 7]
