from datetime import datetime

import random 
import re

def dotw(y, m , d):
    denum = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    day = datetime(y, m, d).weekday()
    return denum[day]
    
def bsearch(l, x, s, e):
    if (e - s) < 0:
        return -1
    b = (s + e) // 2
    if l[b] == x: return b
    elif l[b] > x: return bsearch(l, x, s, b-1)
    else: return bsearch(l, x, b+1, e)

def rl(n):
    return [random.randint(1, 1000) for _ in range(n+1)]

def sl(n):
    return [x for x in range(n+1)]

l = sl(100)

def checker(n):
    for i in range(n+1):
        for j in range(i+1):
            n = [x for x in range(j+1)]
            for k in range(j+1):
                print(f"checking for value {k} in \n{n}")
                print(f"{bsearch(n, k, 0, len(n)-1)}")

def bconv(x, b1, b2):
    alpha = '0123456789abcdefghijklmnopqrstuvxyz'
    n = int(x, b1)
    sign = ''
    res = ''
    if n < 0:
        sign = '-'
        n = -1 * n
    while n > 0:
        q, r = divmod(n, b2)
        res += alpha[r]
        n = q
    return sign + ''.join(reversed(res))


if __name__ == '__main__':
    a1 = bconv('FF', 16, 10)
    assert a1 == '255'

    a2 = bconv('FF', 16, 2)
    assert a2 == '11111111'

    a3 = bconv('-FF', 16, 16)
    assert a3 == '-ff'

    ts = r'''
    there are a24 and z72 in this
    text and s23 b56 that should be replaced.
    '''
    print(re.sub(r'[a-z]{1}[0-9]{2}', '***', ts))