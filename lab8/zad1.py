# Aleksander Kluczka

import numpy as np

def zad1():
    def h(x) -> str:
        x = np.array([int(i) for i in f"{x:07b}"])
        A = np.array([[1, 0, 0, 0],
                      [1, 1, 0, 0],
                      [1, 1, 1, 0],
                      [1, 1, 1, 1],
                      [0, 1, 1, 1],
                      [0, 0, 1, 1],
                      [0, 0, 0, 1]]).transpose()
        retval = np.dot(A, x) % 2
        return ''.join(retval.astype(str))

    for i in range(0b1111111+1):
        result = h(i)
        if result == "0101":
            print(f"{i:03d} - {i:07b} - 0101")


def main():
    zad1()

if __name__ == '__main__':
    main()
