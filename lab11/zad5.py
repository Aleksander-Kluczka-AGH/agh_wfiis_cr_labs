# Aleksander Kluczka


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


def zad5():
    a = multiplicative_inverse(13, 99)
    b = multiplicative_inverse(15, 101)
    print(f"{a=}, {b=}")
    result = chi(4 * a, 56 * b, 99, 101)
    print(f"x = {result}")


def main():
    zad5()


if __name__ == "__main__":
    main()
