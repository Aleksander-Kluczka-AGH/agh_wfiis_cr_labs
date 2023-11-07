import math
import matplotlib.pyplot as plt

def zad3():
    def H(target):
            sum = 0
            for k, v in target.items():
                if v == 0:
                    continue
                sum += v * math.log2(v)
            return -sum

    def coin_entropy(o, r):
        Pr = {
            'o': o,
            'r': r
        }
        return H(Pr)

    print(f"{coin_entropy(0.5, 0.5)=}")
    print(f"{coin_entropy(1.0/4.0, 3.0/4.0)=}")
    print(f"{coin_entropy(99.0/100.0, 1.0/100.0)=}")

    def calc():
        retval = []
        for i in range(1, 31):
            p = 2**i
            retval.append(coin_entropy((p-1)/p, 1/p))
        return retval

    plt.title("Entropy of a biased coin, y = entropy, x = power of 2")
    plt.plot(calc())
    plt.show()


def main():
    zad3()

if __name__ == '__main__':
    main()
