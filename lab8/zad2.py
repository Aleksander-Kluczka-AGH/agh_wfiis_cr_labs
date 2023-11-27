# Aleksander Kluczka

import numpy as np

def zad2():
    M = 365
    Q = [i for i in range(15, 31)]

    def eps(M, Q):
        mult = 1.0
        for i in range(1, Q):
            mult *= float((M - i) / M)
        return 1 - mult

    def eps_approx(M, Q):
        return 1 - np.exp((-Q * (Q - 1)) / (2 * M))

    print(f" Q  | eps     | eps_approx")
    print(f"----+---------+-----------")
    for q in Q:
        print(f"{q:3d} | {eps(M, q):.5f} | {eps_approx(M, q):.5f}")


def main():
    zad2()

if __name__ == '__main__':
    main()
