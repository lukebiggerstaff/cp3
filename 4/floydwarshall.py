from math import inf


def floydwarshall(am):
    n = len(am)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])


if __name__ == "__main__":
    am = [
        [0, inf, inf, inf, 1],
        [inf, 0, inf, 3, 6],
        [6, 2, 0, 7, inf],
        [inf, inf, inf, 0, 5],
        [inf, inf, inf, inf, 0],
    ]
    floydwarshall(am)
    assert am[2] == [6, 2, 0, 5, 7]
