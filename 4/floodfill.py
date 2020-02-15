def floodfill(am, row, col, c1, c2):
    """
    takes in a graph in the form of an adjacency matrix and returns
    a graph changing one character x to the next character y
    """

    dr = [1, 1, 0, -1, -1, -1, 0, 1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    def find_size(r, c):
        if r < 0 or r > len(am) - 1 or c < 0 or c > len(am[r]) - 1:
            return 0
        if am[r][c] != c1:
            return 0
        am[r][c] = c2
        ans = 1
        for d in range(8):
            ans += find_size(r + dr[d], c + dc[d])
        return ans

    return find_size(row, col)


def print_m(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    am = [
        ["l", "l", "l", "l", "l"],
        ["l", "w", "l", "l", "l"],
        ["l", "l", "w", "w", "l"],
        ["l", "w", "w", "w", "l"],
        ["l", "l", "w", "l", "l"],
        ["l", "l", "l", "l", "l"],
    ]
    ans = [
        ["l", "l", "l", "l", "l"],
        ["l", ".", "l", "l", "l"],
        ["l", "l", ".", ".", "l"],
        ["l", ".", ".", ".", "l"],
        ["l", "l", ".", "l", "l"],
        ["l", "l", "l", "l", "l"],
    ]
    print_m(am)
    res3 = floodfill(am, 1, 1, "w", ".")
    print_m(am)
    assert res3 == 7
    assert am == ans

