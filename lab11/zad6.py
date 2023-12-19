# Aleksander Kluczka

import math


def nwd(j, k):
    if j == 0:
        return k
    r = k % j
    return nwd(r, j)


def nwd_expanded(j, k):
    if j == 0:
        return k, 0, 1
    r = k % j
    d, xp, yp = nwd_expanded(r, j)
    x = yp - (k // j) * xp
    y = xp
    return d, x, y


def multiplicative_inverse(a, n):
    d, x, y = nwd_expanded(a, n)
    reverse_a = x % n
    assert (a * reverse_a) % n == 1
    return reverse_a


def chi(a1, a2, m1, m2):
    M = m1 * m2
    M1 = M // m1
    M2 = M // m2
    y1 = multiplicative_inverse(M1, m1)
    y2 = multiplicative_inverse(M2, m2)
    return ((a1 * M1 * y1) + (a2 * M2 * y2)) % M


def square_power(a, e, n):
    d = 1
    e_bin = f"{e:b}"
    s = len(e_bin) - 1
    assert s <= math.log2(n)
    while s >= 0:
        d = (d * d) % n
        if e_bin[s - 1] == "1":
            d = (d * a) % n
        s -= 1
    return d


def zad6():
    def lecture():
        p = 23
        g = 5

        a = 6
        A = square_power(g, a, p)

        b = 15
        B = square_power(g, b, p)
        print(f"{A=}, {B=}")
        alicja_s = square_power(B, a, p)
        bob_s = square_power(A, b, p)
        print(f"{alicja_s=}, {bob_s=}\n")

    def next():
        p = 12987461
        g = 3606738

        a = 357
        b = 199

        A = square_power(g, a, p)
        B = square_power(g, b, p)
        print(f"{A=}, {B=}")
        alicja_s = square_power(B, a, p)
        bob_s = square_power(A, b, p)
        print(f"{alicja_s=}, {bob_s=}")

    lecture()
    next()


def main():
    zad6()


if __name__ == "__main__":
    main()
