from enum import Enum
from math import inf
from queue import PriorityQueue


def dijkstra(al, start):
    state = Enum("state", "unvisited, visited")
    status = [state.unvisited for _ in range(len(al))]
    dist = [inf for _ in range(len(al))]
    dist[start] = 0
    q = PriorityQueue(maxsize=0)
    q.put((0, start))
    while not q.empty():
        cdist, curr = q.get()
        if status[curr] == state.unvisited:
            for neighbor, weight in al[curr]:
                total_dist = cdist + weight
                q.put((total_dist, neighbor))
                dist[neighbor] = min(total_dist, dist[neighbor])
        status[curr] = state.visited
    return dist


if __name__ == "__main__":
    al = [[(4, 1)], [(3, 3), (4, 6)], [(1, 2), (0, 6), (3, 7)], [(4, 5)], []]
    res = dijkstra(al, 2)
    assert res == [6, 2, 0, 5, 7]
