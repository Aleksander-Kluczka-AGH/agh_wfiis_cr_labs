# Aleksander Kluczka

import random

# wynik:
# 561 - z
# 1729 - z
# 6601 - z
# 881 - p
# 9677 - p
# 17371 - p
# 37579 - p


def witness(a, n):
    t, u = 0, n - 1
    while u % 2 == 0:
        t += 1
        u //= 2
    assert t >= 1
    assert u % 2 == 1
    assert n - 1 == pow(2, t) * u
    x_0 = pow(a, u, n)
    x_i1 = x_0
    for _ in range(t):
        x_i = pow(x_i1, 2, n)
        if (x_i == -1) and (x_i1 != 1) and (x_i1 != (n - 1)):
            return True
        x_i1 = x_i

    if x_i != 1:
        return True
    return False


def miller_rabin(n, s):
    for j in range(s):
        a = random.randint(1, n - 1)
        if witness(a, n):
            return False
    return True


def zad1():
    input = [561, 1729, 6601, 881, 9677, 17321, 37579]
    for number in input:
        print(f"{number} - {'p' if miller_rabin(number, 50) else 'z'}")


def main():
    zad1()


if __name__ == "__main__":
    main()
