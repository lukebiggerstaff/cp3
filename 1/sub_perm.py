from itertools import chain, combinations, permutations
from random import randint

# def subs(l):
#     if l == []:
#         return [[]]
#     x = subs(l[1:])
#     res =  x + [[l[0]] + y for y in x]
#     return res

def pset(s):
    if type(s) != list:
        s = list(s)
    for r in range(len(s)+1):
        yield from combinations(s, r)

# def powerset(s):
#     n = len(s)
#     for i in range(1 << n):
#         yield [s[j] for j in range(n) if (i & (i << j))]


if __name__ == '__main__':
    for i in pset(range(4)):
        print(i)