class Fenwick:
    """
    takes a lst of numbers and creates a fenwick tree a.k.a. a binary indexed tree
    a fenwick tree is a tree with parent and child nodes based on the binary
    representation of the integer index. it is a 1-based array that takes O(n+1)
    storage for a 0-based lst. Initialization of the Fenwick tree takes O(n) time
    and allows for the update operation in O(log n) and range queries in O(log n).
    """

    def __init__(self, lst):
        self.ft = [0] + lst
        n = len(lst)
        for i in range(1, n):
            j = i + self._lsb(i)
            if j < n:
                self.ft[j] += self.ft[i]

    def _lsb(self, i):
        """zeros out all but the least significant bit of i"""
        return i & -i

    def _psum(self, i):
        res = 0
        i += 1  # adjust for 1-based arr self.ft
        while i:
            res += self.ft[i]
            i -= self._lsb(i)
        return res

    def update(self, i, amt):
        """update i and parent nodes + amt"""
        n = len(self.ft)
        i += 1  # adjust for 1-based arr self.ft
        while i < n:
            self.ft[i] += amt
            i += self._lsb(i)

    def range_query(self, i, j):
        """returns the sum of all indices between [i..j] inclusive"""
        return self._psum(j) - self._psum(i - 1)

    def __repr__(self):
        return str(self.ft)


if __name__ == "__main__":
    l = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    b = Fenwick(l)
    n = len(l)
    for i in range(n):
        j = b._psum(i)
        k = sum(l[: i + 1])
        assert k == j

    l[1] += 2
    b.update(1, 2)
    l[2] -= 2
    b.update(2, -2)
    for i in range(n):
        j = b._psum(i)
        k = sum(l[: i + 1])
        assert k == j

    for i in range(n):
        for j in range(i):
            rq = b.range_query(j, i)
            s = sum(l[j : i + 1])
            assert rq == s
