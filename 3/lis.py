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
    subs = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if l[j] < l[i]:
                # subs[i] is either the same as before
                # or whatever the value in subs[j] + 1
                subs[i] = max(subs[j] + 1, subs[i])
    max_value = 0
    # iterate over subs to find highest value for
    # the longest increasing subsequence
    for val in subs:
        if val > max_value:
            max_value = val
    return max_value


if __name__ == "__main__":
    l = [-7, 10, 9, 2, 3, 8, 8, 1]
    res = lis(l)
    assert res == 4
