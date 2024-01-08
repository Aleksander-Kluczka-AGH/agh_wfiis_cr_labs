# Aleksander Kluczka


def rule_3(sign, upper, lower):
    power = 0
    while upper % 2 == 0:
        upper //= 2
        power += 1

    if power % 2 == 1:
        sign = -1 * sign

    return sign, upper, lower


def rule_4(sign, upper, lower):
    if (upper % 4 == 3) and (lower % 4 == 3):
        return -1 * sign, lower, upper
    else:
        return 1 * sign, lower, upper


def rule_2(sign, upper, lower):
    if (lower % 8) in [1, 7]:
        return 1 * sign, 1, lower
    elif (lower % 8) in [3, 5]:
        return -1 * sign, 1, lower


def rule_1(sign, upper, lower):
    return sign, upper % lower, lower


def solve_jacobi_symbol(upper, lower):
    org_upper: int = upper + 0
    org_lower: int = lower + 0
    print(f"Solving Jacobi symbol ({upper}/{lower}):")
    sign = 1

    while True:
        if upper == 1:
            print(f"  Final calc result: {'-' if sign < 0 else ' '}({upper}/{lower})")
            break
        if upper == 2:
            print(f"  Applying rule 2 on {'-' if sign < 0 else ' '}({upper}/{lower})")
            sign, upper, lower = rule_2(sign, upper, lower)
            continue
        if upper < lower:
            if upper % 2 == 1:
                print(
                    f"  Applying rule 4 on {'-' if sign < 0 else ' '}({upper}/{lower})"
                )
                sign, upper, lower = rule_4(sign, upper, lower)
            else:
                print(
                    f"  Applying rule 3 on {'-' if sign < 0 else ' '}({upper}/{lower})"
                )
                sign, upper, lower = rule_3(sign, upper, lower)
        elif upper > lower:
            print(f"  Applying rule 1 on {'-' if sign < 0 else ' '}({upper}/{lower})")
            sign, upper, lower = rule_1(sign, upper, lower)

    print(f"  Result ({org_upper}/{org_lower}): {sign * upper}\n")
    return sign * upper


def zad4():
    solve_jacobi_symbol(7411, 9283)  # test
    solve_jacobi_symbol(610, 987)  # a
    solve_jacobi_symbol(20964, 1987)  # b
    solve_jacobi_symbol(1234567, 11111111)  # c


def main():
    zad4()


if __name__ == "__main__":
    main()
