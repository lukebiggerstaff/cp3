from itertools import permutations


def cstsp(al, print_distance=False):
    """
    iterative complete search algorithm for traveling salesman problem. 
    this implementation iterates over all permutations and calculates the total
    for each route and compares against a global minimum route
    """
    min_dist = 1 << 20
    for p in permutations(range(1, len(al))):
        dist = 0
        # add distance from 0 to first city on tour
        dist += al[0][p[0]]  # + al[p[1]][0]
        for i in range(1, len(p)):
            dist += al[p[i - 1]][p[i]]
        # add distance from last city on tour to 0
        dist += al[p[i]][0]
        # print route and distance traveled
        if print_distance:
            print(f"{p} = {dist}")
        min_dist = min(dist, min_dist)

    return min_dist


def bitsp(al):
    """
    complete search algorithm for traveling salesman problem. This recursive implementation uses a bitmask
    to track visited locations 
    """

    def best_route(i, mask=1):
        # if all cities have been visited return
        # distance to 0
        if mask == (1 << len(al)) - 1:
            return al[i][0]
        total_min = 1 << 20
        for nxt in range(len(al[i])):
            # iterate if city is unvisited and
            # next city does not equal current
            if not mask & (1 << nxt) and nxt != i:
                min_i = al[i][nxt] + best_route(nxt, mask | (1 << nxt))
                total_min = min(total_min, min_i)
        return total_min

    return best_route(0)


def tdbitsp(al):
    """
    top down dp algorithm for solving the traveling salesman problem. 
    This recursive implementation uses a bitmask to track visited locations 
    """

    # store state information to solve overlapping sub-problems
    states = dict()

    def best_route(i, mask=1):
        if mask == (1 << len(al)) - 1:
            return al[i][0]
        # initialize min_route to large integer
        min_route = 1 << 20
        # initialize key to store state
        key = (i, mask)
        if key in states:
            return states[key]
        for nxt in range(len(al[i])):
            if not mask & (1 << nxt) and nxt != i:
                route = al[i][nxt] + best_route(nxt, mask | (1 << nxt))
                min_route = min(min_route, route)
        states[key] = min_route
        return states[key]

    return best_route(0)


if __name__ == "__main__":
    al = [
        [0, 20, 42, 35, 15],
        [20, 0, 30, 34, 20],
        [42, 30, 0, 12, 20],
        [35, 34, 12, 0, 15],
        [15, 30, 12, 20, 0],
    ]

    res = cstsp(al)
    assert res == 92

    res2 = bitsp(al)
    assert res2 == 92

    res3 = tdbitsp(al)
    assert res3 == 92
