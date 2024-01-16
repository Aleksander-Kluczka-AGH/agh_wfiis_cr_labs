# Aleksander Kluczka


def nwd_expanded(j, k):
    if j == 0:
        return k, 0, 1
    r = k % j
    d, xp, yp = nwd_expanded(r, j)
    x = yp - (k // j) * xp
    y = xp
    return d, x, y


def pollard_p_minus_1(n: int, b: int) -> int | None:
    a: int = 2
    for j in range(2, b + 1):
        a = pow(a, j, n)
    d: int = nwd_expanded(a - 1, n)[0]
    if 1 < d < n:
        return d
    else:
        return None


def pollard_p_minus_1_with_search(n: int) -> tuple[int, int]:
    b = 2
    result = None
    while True:
        result = pollard_p_minus_1(n, b)
        if result is not None:
            break
        b += 1
    return result, b


def zad2():
    number_1 = 262063
    number_2 = 9420457

    result_1, b_1 = pollard_p_minus_1_with_search(number_1)
    print(f"pollard_p1({number_1}) = {result_1}, minimum b = {b_1}")

    result_2, b_2 = pollard_p_minus_1_with_search(number_2)
    print(f"pollard_p1({number_2}) = {result_2}, minimum b = {b_2}")


def main():
    zad2()


if __name__ == "__main__":
    main()
