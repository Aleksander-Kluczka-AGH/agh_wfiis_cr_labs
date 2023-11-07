import matplotlib.pyplot as plt


def zad3():
    def parity(y_i) -> int:
        parity = 0
        while True:
            parity += y_i & 1
            y_i = y_i >> 1
            if not y_i:
                break
        return parity % 2


    def blumblumshub(p, q, s):
        n = p * q
        y = []
        z = ""
        for i in range(0, n):
            y_im1 = s if i == 0 else y[i-1]
            y_i = ((y_im1*y_im1) % n)
            y.append(y_i)

            z_i = parity(y_i)
            z += chr(z_i + ord('0'))

        plt.title(f"{p=}, {q=}, {s=}")
        plt.yscale("log")
        plt.plot(y, 'o-', linewidth=0.1, markersize=0.3)
        plt.show()

        return z[1::]

    def search(seq):
        max_len = len(seq) // 2
        for length in range(1, max_len):
            for y in range(0, max_len, length):
                if len(seq[y:y+length]) < length:
                    break
                if seq[0:length] != seq[y:y+length]:
                    break
            else:
                return length

        return 0



    print("a: ")
    a = blumblumshub(7, 19, 100)
    print(f"{a}")
    a_cycle = search(a)
    print(f"{a_cycle=}")

    print("v: ")
    b = blumblumshub(67, 71, 100)
    print(f"{b}")
    b_cycle = search(b)
    print(f"{b_cycle=}")

    print("v: ")
    c = blumblumshub(163, 167, 100)
    print(f"{c}")
    c_cycle = search(c)
    print(f"{c_cycle=}")


def main():
    zad3()

if __name__ == '__main__':
    main()
