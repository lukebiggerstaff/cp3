def coinchange(coins, total):
    """
    an algorithm to make change from given list of coins and a total value
    implementation searches all possible combination and returns the
    minimum amount of coins used
    """

    def make_change(i, v):
        # if v is 0 then no further coins are needed
        # to make change
        if v == 0:
            return 0
        # if v is less than 0 or v is not zero and i
        # is past the last coin then return
        # a very large number to signify this path was impossible
        if v < 0 or i >= len(coins):
            return 10 ** 20
        # if the value of the current coin i is less than
        # the remaining value
        if coins[i] <= v:
            # find the minimum of the two branches
            # one of which uses this coin and the other
            # does not
            return min(make_change(i + 1, v), 1 + make_change(i, v - coins[i]))
        return make_change(i + 1, v)

    return make_change(0, total)


def tdcchange(coins, total):
    """
    algorithm to make change from a given list of coins and a total value
    the implementation is a top-down dynamic programming algorithm that stores
    results in a memo dictionary for lookup.
    """

    memo = dict()

    def make_change(i, v):
        if v == 0:
            return 0
        if v < 0 or i >= len(coins):
            return 10 ** 20
        # create key for current state
        # coin i and remaining value v
        key = (i, v)
        if key in memo:
            return memo[key]
        if coins[i] <= v:
            memo[key] = min(make_change(i + 1, v), 1 + make_change(i, v - coins[i]))
            return memo[key]
        return make_change(i + 1, v)

    return make_change(0, total)


def change_ways(coins, total):
    """
    complete search algorithm to determine the number of ways
    to make change from a total amount given a list of coins
    """

    def ways(i, v):
        # if v is 0 then we have a successful way to make
        # change
        if v == 0:
            return 1
        # if v is less than zero or the coin iterator
        # is beyond all coins then we do not have a way
        if v < 0 or i >= len(coins):
            return 0
        # return the different ways to make change with
        # and without the current coin
        return ways(i, v - coins[i]) + ways(i + 1, v)

    return ways(0, total)


def tdcw(coins, total):
    """
    a top-down dp algorithm to determine the number of different
    ways to make change from a list of coins and an amount
    """

    memo = dict()

    def ways(i, v):
        if v == 0:
            return 1
        if v < 0 or i >= len(coins):
            return 0
        key = (i, v)
        if key in memo:
            return memo[key]
        memo[key] = ways(i, v - coins[i]) + ways(i + 1, v)
        return memo[key]

    return ways(0, total)


if __name__ == "__main__":
    coins = [1, 5]
    value = 12

    res = coinchange(coins, value)
    assert res == 4

    res2 = tdcchange(coins, value)
    assert res2 == 4

    res3 = change_ways(coins, value)
    assert res3 == 3

    res4 = tdcw(coins, value)
    assert res4 == 3
