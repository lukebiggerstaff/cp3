"""
n-queens problem asks where can you place n queens on a n x n chessboard.
"""


def nqueens(a, b, n):

    sol = [None for _ in range(n)]

    def place(r, c, board):
        for prev in range(c):
            # check position of each previous queen and confirm its not on
            # the same row and also confirm the diagonal
            if board[prev] == r or (abs(board[prev] - r) == abs(prev - c)):
                return False
        return True

    def backtrack(a, b, n, c=0, board=None):
        if board is None:
            board = [None for _ in range(n)]
        # check if we have iterated over all columns
        # and that original queen is in correct location
        if c == n and board[b] == a:
            nonlocal sol
            # use list slice operator to copy board to sol
            sol = board[:]
        for r in range(n):
            if place(r, c, board):
                board[c] = r
                backtrack(a, b, n, c + 1, board)

    backtrack(a, b, n)
    return sol


if __name__ == "__main__":
    s = nqueens(1, 0, 4)
    assert s == [1, 3, 0, 2]

    print(f"{nqueens(6, 0, 12)}")
