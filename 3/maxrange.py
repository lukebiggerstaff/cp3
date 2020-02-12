def kadane(l):
    rsum = 0
    ans = 0
    for i in range(len(l)):
        # keep running sum
        rsum += l[i]
        # ans is the running total plus current elem
        # or the previous highest running total
        ans = max(ans, rsum)
        # if rsum is negative start over from 0
        if rsum < 0:
            rsum = 0
    return ans


if __name__ == "__main__":
    l = [-1, 2, -1, 6, -5]
    res = kadane(l)
    assert res == 7
