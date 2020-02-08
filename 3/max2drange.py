def max_sub_rect(mat, n):
    # convert mat into a sum matrix
    # where every entry in mat[i][j]
    # equals the total from [0][0]..[i][j] in mat
    for i in range(n):
        for j in range(n):
            if i > 0:
                mat[i][j] += mat[i - 1][j]
            if j > 0:
                mat[i][j] += mat[i][j - 1]
            if i > 0 and j > 0:
                mat[i][j] -= mat[i - 1][j - 1]
    max_sub = -10 ** 20
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    sub = mat[k][l]
                    if i > 0:
                        sub -= mat[i - 1][l]
                    if j > 0:
                        sub -= mat[k][j - 1]
                    if i > 0 and j > 0:
                        sub += mat[i - 1][j - 1]
                    max_sub = max(max_sub, sub)
    return max_sub


def p_mat(mat):
    for row in mat:
        print(row)
    print()


if __name__ == "__main__":
    mat = [[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]]
    res = max_sub_rect(mat, 4)
    assert res == 15
