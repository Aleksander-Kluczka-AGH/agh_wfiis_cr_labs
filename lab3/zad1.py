from copy import copy

def zad1():
    def a(index, start: list[int]):
        if index < 4:
            return start[index]
        else:
            temp = copy(start)
            for i in range(0, index):
                temp[i % 4] = (temp[(i % 4) - 4] + temp[(i % 4) - 3] + temp[(i % 4) - 2] + temp[(i % 4) - 1]) % 2
            return temp[index % 4]

    def b(index, start: list[int]):
        if index < 4:
            return start[index]
        else:
            temp = copy(start)
            for i in range(0, index):
                temp[i % 4] = (temp[(i % 4) - 4] + temp[(i % 4) - 1]) % 2
            return temp[index % 4]


    def generate(func, start: list[int], length = 50):
        return ''.join([chr(func(i, start) + ord('0')) for i in range(0, length)])

    print(f"Dane testowe:")

    print(f"a - wektor: 0100")
    print(f"a - strumien: {generate(a, [0, 1, 0, 0])}")
    print(f"b - wektor: 1000")
    print(f"b - strumien: {generate(b, [1, 0, 0, 0])}")

    def search(seq):
        guess = 1
        max_len = len(seq)
        for x in range(1, max_len):
            for y in range(1, max_len):
                if seq[0:x] == seq[y:y+x] :
                    guess = x

        return abs(guess - max_len)


    print(f"\nWyniki a:")
    for i in range(0, 16):
        binary = [ord(c) - ord('0') for c in f"{i:04b}"]
        stream = generate(a, binary)
        print(f"P({i:04b})={search(stream)}")


    print(f"\nWyniki b:")
    for i in range(0, 16):
        binary = [ord(c) - ord('0') for c in f"{i:04b}"]
        stream = generate(b, binary)
        print(f"P({i:04b})={search(stream)}")


def main():
    zad1()

if __name__ == '__main__':
    main()
