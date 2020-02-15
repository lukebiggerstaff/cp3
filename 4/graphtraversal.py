from collections import deque


def bfs(al, log):
    """
    breadth first search of a graph in
    adjacency list representation.
    """

    def cprint(s, end="\n"):
        """helper print function to track nodes visited"""
        if log:
            print(s, end=end)

    visited = set()
    queue = deque()
    queue.append(0)
    while queue:
        curr = queue.popleft()
        cprint(f"{curr} -> ", end="")
        for neighbor in al[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    cprint("None")


def dfs(al, log):
    """
    depth first search of a graph in al form
    """

    visited = set()

    def cprint(s, end="\n"):
        """helper print function to track nodes visited"""
        if log:
            print(s, end=end)

    def rdfs(i):
        cprint(f"{i} -> ", end="")
        for neighbor in al[i]:
            if neighbor not in visited:
                visited.add(neighbor)
                rdfs(neighbor)

    rdfs(0)
    cprint("None")


if __name__ == "__main__":
    al = [[1, 3], [2], [3], [2, 1]]

    bfs(al, False)
    dfs(al, False)
