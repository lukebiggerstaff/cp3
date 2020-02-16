from enum import Enum


def graph_edge_check(al):
    """
    algorithm that classifies edges of a graph 
    into one of three types
    1) Tree edge - edge from vertex with state explored
        to vertex with state: unvisited
    2) Back edge - edge that is part of a cycle. i.e. 
        an edge rom a vertex currently with state: 
        explored to a vertex with state explored
    3) Foward/ Cross Edge - edge from vertex with state:
        explored to a vertex with state: visited.
    """

    node = Enum("node", "UNVISITED, EXPLORED, VISITED")
    state = [node.UNVISITED for _ in range(len(al))]
    parent = [v for v in range(len(al))]
    component_num = 1

    def dfs(u):
        state[u] = node.EXPLORED
        for v in al[u]:
            if state[v] == node.UNVISITED:
                parent[v] = u
                dfs(v)
            elif state[v] == node.EXPLORED:
                if v == parent[u]:
                    print(f"  Two-way edge ({u}, {v}), ({v}, {u})")
                else:
                    print(f"  Back Edge ({u}, {v}) Cycle")
            elif state[v] == node.VISITED:
                print(f"  Forward/Cross Edge ({u}, {v})")
        state[u] = node.VISITED

    for u, status in enumerate(state):
        if status == node.UNVISITED:
            print(f"Component {component_num})")
            component_num += 1
            dfs(u)


if __name__ == "__main__":
    al = [[1], [0, 2, 3], [1, 3], [1, 2, 4], [3], [], [7, 8], [6], [6]]
    graph_edge_check(al)
