def outerg():
    x = 2

    def inner():
        global x
        print(f"\t\tglobal x from inner = {x}")

    print(f"\tx from outer = {x}")
    inner()
    print(f"\tx from outer = {x}\n")


def outern():
    x = 2

    def inner():
        nonlocal x
        print(f"\t\tnonlocal x from inner = {x}")

    print(f"\tx from outer = {x}")
    inner()
    print(f"\tx from outer = {x}\n")


def outera():
    x = 2

    def inner():
        x = 3
        print(f"\t\tx assigned from inner = {x}")

    print(f"\tx from outer = {x}")
    inner()
    print(f"\tx from outer = {x}\n")


def outeran():
    x = 2

    def inner():
        nonlocal x
        x = 3
        print(f"\t\tnonlocal x assigned from inner = {x}")

    print(f"\tx from outer = {x}")
    inner()
    print(f"\tx from outer = {x}\n")


def outerag():
    x = 2

    def inner():
        global x
        x = 3
        print(f"\t\tglobal x assigned from inner = {x}")

    print(f"\tx from outer = {x}")
    inner()
    print(f"\tx from outer = {x}\n")


if __name__ == "__main__":
    x = 1
    print(f"global x = {x}")
    outerg()
    outern()
    outera()
    outeran()
    outerag()
    print(f"global x = {x}")
