if __name__ == "__main__":
    # bit operations
    s = 34
    j = 3

    s |= 1 << j  # set jth bit using OR
    assert s == 42

    t = s & (1 << j)  # check if jth bit is set using AND
    assert t == (1 << j)  # if bit is set it will equal j

    s &= ~(1 << j)  # turn off jth bit using NOT
    assert s == 34

    b = s & (1 << j)  # check if jth bit is set using AND
    assert b == 0  # if bit is not set it will equal 0

    s ^= 1 << j  # toggle the jth bit using XOR
    assert s == 42
    s ^= 1 << j  # toggle the jth bit using XOR
    assert s == 34

    t = s & (~s)  # get value from LSB
    assert t == 0

    n = 5
    s = (1 << n) - 1  # set all values of size n
    assert s == 31

    # check if number n is even or odd
    n = 35
    assert n & 1 == 1
    n = 34
    assert n & 1 == 0

    # determine if n is a power of 2
    # power of 2 has form of 10 = 2 100 = 4 1000 = 8
    # taking the bitwise AND of a power of 2 minus 1 will result in 0
    # example: 2 - 1 = 1 2=10 1=1, 8 - 1 = 7 8=1000
    for n in range(11):
        k = 2 ** n
        assert k and not (k & (k - 1))

    # take remainder of division by power of 2
    n = 9
    d = 4
    assert n & (d - 1) == 1

    # Detect if two integers have opposite signs
    x = 8
    y = -9
    assert ((x ^ y) < 0) == True
    y = 9
    assert ((x ^ y) < 0) == False

    # two's complement stores postive integers up to 2^n - 1,
    # and negative up to 2^n with n=32 or n=64
    # the last spot is reserved for the negative sign.
    # examples
    # 2  = 00000010
    # 1  = 00000001
    # 0  = 00000000
    # -1 = 11111111
    # -2 = 11111110
    # from the above you can see that adding one to a two's complement negative number
    # will result in the correct binary number.

    # convert from positive number to negative two's complement
    x = 5  # 101
    print(f"x={x}:{bin(x)}")
    y = (~x) + 1  # 1101
    print(f"y={y}:{bin(y)}")
    assert y == -5

    # turn off last bit set
    n = v = 11  # 11 = 1011
    j = 0
    print(f"turn off last bit set n={n}: {bin(n)}")
    while v != 0:  # iterate length of bit from right to left
        if v & 1:  # take AND 1 to check if first bit is set
            n &= ~(1 << j)  # flip bit at jth counter via XOR
            break
        v >>= 1  # right shift v by one
        j += 1  # increment j by 1
    print(f"n={n}: {bin(n)}")

    # turn on first zero
    n = v = 9
    j = 0
    print(f"turn on first zero n={n}: {bin(n)}")
    while v != 0:
        if not (v & 1):
            n |= 1 << j
            break
        v >>= 1
        j += 1
    print(f"n={n}: {bin(n)}")

    # turn off last consecutive run of 1's
    n = v = 39
    j = 0
    mask = 0
    print(f"turn off last consecutive run of 1's\nn={n}: {bin(n)}")
    while v != 0:
        if v & 1:
            mask |= 1 << j
        else:
            break
        v >>= 1
        j += 1
    n &= ~mask
    print(f"n={n}: {bin(n)}")

    # turn on last consecutive run of 0's
    n = v = 32
    j = 0
    mask = 0
    print(f"turn on last consecutive run of 0's\nn={n}: {bin(n)}")
    while v != 0:
        if not (v & 1):
            mask |= 1 << j
        else:
            break
        v >>= 1
        j += 1
    n |= mask
    print(f"n={n}: {bin(n)}")

    # swap variables without use of extra variable
    a = 10
    b = 20
    print(f"a={bin(a)}, b={bin(b)}")
    a ^= b
    print(f"a={bin(a)}, b={bin(b)}")
    b ^= a
    print(f"a={bin(a)}, b={bin(b)}")
    a ^= b
    print(f"a={bin(a)}, b={bin(b)}")

