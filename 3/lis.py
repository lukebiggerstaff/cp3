def cslis(l):
    """
    complete search algorithm for finding
    the longest increasing subsequence
    """

    def pset(l):
        n = len(l)
        for i in range(1, (1 << n)):
            yield [l[j] for j in range(n) if (i & (1 << j))]

    max_value = 0
    for ss in pset(l):
        for i in range(1, len(ss)):
            if ss[i - 1] > ss[i]:
                break
            elif i >= len(ss) - 1:
                max_value = max(max_value, len(ss) - 1)
    return max_value


def lis(l):
    """
    the longest increasing subsequence is the longest stretch
    where each preceding element (but not necessarly contiguous)
    in the subsequence is less than the next element. The trick
    is to iterate through every subsequence from j to i and keep
    track of the longest subsequence at every i.
    """
    n = len(l)
    # initialize subs list to hold subsequence values
    max_value = 0
    subs = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if l[j] < l[i]:
                # subs[i] is either the same as before
                # or whatever the value in subs[j] + 1
                subs[i] = max(subs[j] + 1, subs[i])
                # update max_value while iterating
                max_value = max(subs[i], max_value)
    return max_value


if __name__ == "__main__":
    l = [-7, 10, 9, 2, 3, 8, 8, 1]

    res = lis(l)
    assert res == 4

    res2 = cslis(l)
    assert res2 == 4
