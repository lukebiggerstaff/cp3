def csknap(s, v, w):
    """
    0/1 knapsack implemented as a recursive complete search algorithm
    """

    def val(item, remw):
        # return 0 if there is no weight left
        # or you have iterated past the end of items
        if remw <= 0 or item >= len(v):
            return 0
        # if item weight fits into remaining weight
        # see if the overall value is better w or w/out item
        if w[item] <= remw:
            return max(v[item] + val(item + 1, remw - w[item]), val(item + 1, remw))
        return val(item + 1, remw)

    return val(0, s)


def tdknap(s, v, w):
    """
    0/1 knapsack implemented as a recursive top-down
    dynamic programming algorithm 
    """
    memo = dict()

    def val(item, remw):
        if remw <= 0 or item >= len(v):
            return 0
        state = (item, remw)
        if state in memo:
            return memo[state]
        if w[item] <= remw:
            memo[state] = max(
                v[item] + val(item + 1, remw - w[item]), val(item + 1, remw)
            )
            return memo[state]
        return val(item + 1, remw)

    return val(0, s)


def buknap(s, v, w):
    """
    0/1 knapsack implementation via bottom-up dp
    s is total capacity, v is value of object 
    and w is weight of object
    """
    items = len(v)
    weights = s
    mat = [[0 for _ in range(weights + 1)] for _ in range(items + 1)]
    for i in range(1, items + 1):
        for j in range(weights + 1):
            if w[i - 1] <= j:
                mat[i][j] = max(mat[i - 1][j], mat[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                mat[i][j] = mat[i - 1][j]
    return mat[i][j]


if __name__ == "__main__":
    v = [100, 80, 90, 10, 70, 50]
    w = [10, 4, 8, 12, 4, 6]
    s = 12

    res = csknap(s, v, w)
    assert res == 170

    res2 = tdknap(s, v, w)
    assert res2 == 170

    res3 = buknap(s, v, w)
    assert res3 == 170

