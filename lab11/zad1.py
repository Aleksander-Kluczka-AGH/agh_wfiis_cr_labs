# Aleksander Kluczka


def nwd(j, k):
    if j == 0:
        return k
    r = k % j
    return nwd(r, j)


def nwd_expanded(j, k):
    assert 0 <= j < k
    if j == 0:
        return k, 0, 1
    r = k % j
    d, xp, yp = nwd_expanded(r, j)
    x = yp - (k // j) * xp
    y = xp
    return d, x, y


def zad1():
    j, k = 57, 93
    result = nwd(57, 93)
    print(f"nwd({j}, {k}) = {result}")
    d, s, t = nwd_expanded(57, 93)
    assert (j * s + k * t) == result
    print(f"{s=}, {t=}")


def main():
    zad1()


if __name__ == "__main__":
    main()
