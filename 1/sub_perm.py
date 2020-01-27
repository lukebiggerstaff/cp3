from itertools import combinations, permutations
from random import randint

def subs(l):
    if l == []:
        return [[]]
    x = subs(l[1:])
    res =  x + [[l[0]] + y for y in x]
    return res

def pset(s):
    if type(s) != list:
        s = list(s)
    for r in range(len(s)+1):
        yield from combinations(s, r)

if __name__ == '__main__':
    for i in pset(range(4)):
        print(i)
    
    # generate all possible permutations of N=10 letters of alphabet
    for i in permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']):
        print(i)