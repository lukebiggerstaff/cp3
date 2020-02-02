inf = 10 ** 20


def left(i):
    # left shift i by one
    return i << 1


def right(i):
    # left shift i by one and add 1
    return (i << 1) + 1


def sum_st(a, p, l, r, st=None):
    """segment tree that stores the sum of ranges of an array"""
    # initialize st to 3 times array size
    if st is None:
        st = [None] * (len(a) * 3)
    # traversed the tree to the leaf, set the value
    if l == r:
        st[p] = a[l]
    else:
        mid = (l + r) // 2
        sum_st(a, left(p), l, mid, st)
        sum_st(a, right(p), mid + 1, r, st)
        # st is the sum of all values in the range
        st[p] = st[left(p)] + st[right(p)]
    return st


def update_st(a, st, p, l, r, i, v):
    """O(log n) update to array and segment tree"""
    if l == r:
        a[i] += v
        st[p] += v
    else:
        # split tree in half and traverse until we reach leaf node at i
        mid = (l + r) // 2
        if l <= i and i <= mid:
            update_st(a, st, left(p), l, mid, i, v)
        else:
            update_st(a, st, right(p), mid + 1, r, i, v)
        st[p] = st[left(p)] + st[right(p)]


def min_st(a, p, l, r, st=None):
    """creates a min segment tree from array a, that stores the minimum of a range"""
    if st is None:
        st = [None] * (len(a) * 3)
    if l == r:
        st[p] = a[l]
    else:
        mid = (l + r) // 2
        min_st(a, left(p), l, mid, st)
        min_st(a, right(p), mid + 1, r, st)
        # st is the minimum of values in the range
        st[p] = min(st[left(p)], st[right(p)])
    return st


def max_st(a, p, l, r, st=None):
    """creates a max segment tree from array a, that stores the maximum of a range"""
    if st is None:
        st = [None] * (len(a) * 3)
    if l == r:
        st[p] = a[r]
    else:
        mid = (l + r) // 2
        max_st(a, left(p), l, mid, st)
        max_st(a, right(p), mid + 1, r, st)
        # st is the max of values in the range
        st[p] = max(st[left(p)], st[right(p)])
    return st


def rminq(st, p, l, r, i, j):
    """range query for the minimum value from a min seg tree"""
    # no overlap return inf
    if l > j or r < i:
        return inf
    # total overlap return segment value
    elif l >= i and r <= j:
        return st[p]
    # partial overlap return min of both sides of segment tree
    else:
        mid = (l + r) // 2
        return min(
            rminq(st, left(p), l, mid, i, j), rminq(st, right(p), mid + 1, r, i, j)
        )


def rsumq(st, p, l, r, i, j):
    """range query for the sum of values from a range on a sum seg tree"""
    # no overlap return 0
    if l > j or r < i:
        return 0
    # total overlap return st node
    elif l >= i and r <= j:
        return st[p]
    # partial overlap return value from both side
    else:
        mid = (l + r) // 2
        return rsumq(st, left(p), l, mid, i, j) + rsumq(st, right(p), mid + 1, r, i, j)


if __name__ == "__main__":
    assert left(1) == 2
    assert right(1) == 3
    lst = [1, 1]
    st = sum_st(lst, 1, 0, len(lst) - 1)
    assert st[:4] == [None, 2, 1, 1]

    lst = [1, 1, 1, 1, 1, 1]
    st = sum_st(lst, 1, 0, len(lst) - 1)
    print(f"{st}")
    print(f"{lst}")
    assert st[:14] == [None, 6, 3, 3, 2, 1, 2, 1, 1, 1, None, None, 1, 1]
    update_st(lst, st, 1, 0, len(lst) - 1, 2, 4)
    assert lst[2] == 5
    print(f"{st}")
    print(f"{lst}")

    n = len(lst) - 1
    m = rsumq(st, 1, 0, n, 0, 6)
    print(f"{st}")
    print(f"{lst}")
    print(f"{m}")

    lst = [-1, 3, 4, 0, 2, 1]
    st = min_st(lst, 1, 0, len(lst) - 1)
    n = len(lst) - 1
    m = rminq(st, 1, 0, n, 1, 3)
    print(f"{st}")
    print(f"{lst}")
    print(f"{m}")
