# Aleksander Kluczka


def multiplicative_inverse(a, n):
    def nwd_expanded(j, k):
        if j == 0:
            return k, 0, 1
        r = k % j
        d, xp, yp = nwd_expanded(r, j)
        x = yp - (k // j) * xp
        y = xp
        return d, x, y

    d, x, y = nwd_expanded(a, n)
    reverse_a = x % n
    assert (a * reverse_a) % n == 1
    return reverse_a


def zad2():
    p = 1511
    q = 2003
    d = 1234577
    dp = d % (p - 1)
    dq = d % (q - 1)
    mp = multiplicative_inverse(q, p)
    mq = multiplicative_inverse(p, q)
    n = (p - 1) * (q - 1)

    print(f"{dp=}, {dq=}, {mp=}, {mq=}")

    def ctr(n, dp, dq, mp, mq, y):
        xp = pow(y, dp, p)
        xq = pow(y, dq, q)
        print(f"{xp=}, {xq=}")
        x = ((mp * q * xp) + (mq * p * xq)) % n
        return x

    x = ctr(n, dp, dq, mp, mq, 152702)
    print(f"{x=}")


def main():
    zad2()


if __name__ == "__main__":
    main()
