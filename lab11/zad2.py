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


def multiplicative_inverse(a, n):
    d, x, y = nwd_expanded(a, n)
    reverse_a = x % n
    assert (a * reverse_a) % n == 1
    return reverse_a


def zad2():
    exercises = {
        "a": [17, 101],
        "b": [357, 1234],
        "c": [3125, 9987],
    }

    for exercise, values in exercises.items():
        a, n = values[0], values[1]
        reverse_a = multiplicative_inverse(a, n)
        print(f"{exercise}: {a=:5}, {n=:5}, result={reverse_a:5}")


def main():
    zad2()


if __name__ == "__main__":
    main()
