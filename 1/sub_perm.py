from random import randint


def powerset(s):
    n = len(s)
    for i in range((1 << n)):
        yield [s[j] for j in range(n) if (i & (1 << j))]


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def perm(a, i):
    n = len(a)
    if i == n:
        yield a
    for j in range(i, n):
        swap(a, i, j)
        yield from perm(a, i + 1)
        swap(a, i, j)


if __name__ == "__main__":
    print("generate all subsets of a set")
    for i in powerset(["a", "b", "c"]):
        print(i)

    print("generate all permutations of a set")
    for i in perm(["a", "b", "c"], 0):
        print(i)
