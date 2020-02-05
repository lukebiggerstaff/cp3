"""
iterative complete search is a way to exhaust all combinations 
of the search space and eventually find the answer.
"""

from random import randint
from itertools import combinations, permutations


def locker_combo():
    n = 10
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    yield (a, b, c, d)


def abcxyz(A, B, C):
    """find x, y, z s.t.
        x + y + z = A
        x * y * z = B
        x*x + y*y + z*z = C
    """
    # assume x is the largest number x * x * x = B**(1/3)
    # The cubed root of 10,000 is around 21 and bounds x
    for x in range(-22, 23):
        # if x squared is larger than C prune the search space
        if x ** 2 <= C:
            for y in range(-100, 101):
                # prune search space for y == x
                # and if the two squared values
                # of x and y are larger than C
                if y != x and x * x + y * y <= C:
                    for z in range(-100, 101):
                        # short circuit cases where x or y == z
                        if (
                            x != z
                            and y != z
                            and (x + y + z) == A
                            and (x * y * z) == B
                            and (x ** 2 + y ** 2 + z ** 2) == C
                        ):
                            print(
                                f"{(x, y, z)} A={x + y + z} B={x * y * z} C={x**2+y**2+z**2}"
                            )


def subs(l):
    n = len(l)
    # there are 2**n subsets of l
    s = [[] for _ in range(1 << n)]
    for i in range(1 << n):
        for j in range(n):
            # check if bit is set at j location
            if (1 << j) & i:
                s[i].append(l[j])
    return s


def sum_subset(l, x):
    n = len(l)
    for i in range(1 << n):
        sum = 0
        for j in range(n):
            if (1 << j) & i:
                sum += l[j]
        if sum == x:
            return [l[k] for k in range(1 << n) if (i & (1 << k))]
    return []


if __name__ == "__main__":
    S = [randint(0, 100) for _ in range(6)]
    # print(S)
    # for comb in gen_sub(S):
    #     print(comb)

    # for c in locker_combo():
    #     print(f"{c}")

    # abcxyz(A, B, C)

    l = [1, 2, 3, 4, 5, 6]
    assert sum_subset(l, 4) == [1, 3]
    assert sum(sum_subset(l, 5)) == 5
    assert sum_subset(l, 0) == []

    l = [1, 2, 3, 4]
    print(len(list(combinations(l, len(l)))))
    print(len(list(permutations(l, len(l)))))
    print(len(subs(l)))

