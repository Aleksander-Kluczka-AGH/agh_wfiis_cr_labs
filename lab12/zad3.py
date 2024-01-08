# Aleksander Kluczka


def square_remainders(p):
    return set([pow(i, 2, p) for i in range(p)])


def euler_criteria(p):
    return [0] + [i for i in range(p) if pow(i, (p - 1) // 2, p) == 1]


def zad3():
    square = square_remainders(13)
    print(square)
    euler = euler_criteria(13)
    print(euler)


def main():
    zad3()


if __name__ == "__main__":
    main()
