# Aleksander Kluczka

from typing import Callable


def nwd_expanded(j: int, k: int) -> tuple[int, int, int]:
    if j == 0:
        return k, 0, 1
    r: int = k % j
    d, xp, yp = nwd_expanded(r, j)
    x: int = yp - (k // j) * xp
    y: int = xp
    return d, x, y


def pollard_rho(n: int, x1: int, f_x: Callable) -> tuple[int | None, int]:
    x: int = x1
    xp: int = f_x(x) % n
    p: int = nwd_expanded(abs(x - xp), n)[0]
    iter: int = 0
    while p == 1:
        iter += 1
        x = f_x(x) % n
        xp = f_x(xp) % n
        xp = f_x(xp) % n
        p = nwd_expanded(abs(x - xp), n)[0]
    print(f"pollard_rho({n}, {x1}) = {p} * {n // p}, iter = {iter}")
    print(f"    x_{iter} = {x}, x_{iter *2} = {xp}")
    if p == n:
        return None, iter
    else:
        return p, iter


def zad3():
    number_1 = 262063
    number_2 = 9420457
    number_3 = 181937053
    func = lambda x: x**2 + 1

    pollard_rho(number_1, 1, func)
    pollard_rho(number_2, 1, func)
    pollard_rho(number_3, 1, func)


def main():
    zad3()


if __name__ == "__main__":
    main()
