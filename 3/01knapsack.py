def knap(s, v, w):
    """
    0/1 knapsack implementation, s is total capacity
    v is value of object and w is weight of object
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
    v = [100, 70, 50, 10]
    w = [10, 4, 6, 12]
    s = 12
    res = knap(s, v, w)
    assert res == 120
