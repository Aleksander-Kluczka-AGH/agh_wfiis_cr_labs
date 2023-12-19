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


def chi(a1, a2, a3, m1, m2, m3):
    M = m1 * m2 * m3
    M1 = M // m1
    M2 = M // m2
    M3 = M // m3
    print(f"{M=}, {M1=}, {M2=}, {M3=}")
    y1 = multiplicative_inverse(M1, m1)
    y2 = multiplicative_inverse(M2, m2)
    y3 = multiplicative_inverse(M3, m3)
    print(f"chi^(-1)(x) = {y1}*{a1}, {y2}*{a2}, {y3}*{a3}")
    return ((a1 * M1 * y1) + (a2 * M2 * y2) + (a3 * M3 * y3)) % M


def zad4():
    print(chi(12, 9, 23, 25, 26, 27))


def main():
    zad4()


if __name__ == "__main__":
    main()
