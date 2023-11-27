# Aleksander Kluczka

def zad1():
    x1 = 0b0000000011111111
    x2 = 0b0000111100001111
    x3 = 0b0011001100110011
    x4 = 0b0101010101010101

    y1 = 0b1010011101010100
    y2 = 0b1110010000111001
    y3 = 0b1000111011100001
    y4 = 0b0011011010001101

    print(f"x1: {x1:016b}")
    print(f"x2: {x2:016b}")
    print(f"x3: {x3:016b}")
    print(f"x4: {x4:016b}\n")

    print(f"y1: {y1:016b}")
    print(f"y2: {y2:016b}")
    print(f"y3: {y3:016b}")
    print(f"y4: {y4:016b}\n")

    def pr(val, bit) -> float:
        val_str = f"{val:016b}"
        return val_str.count(str(bit)) / len(val_str)

    def eps(val, bit) -> float:
        return pr(val, bit) - 0.5

    x1_x4_y2 = x1 ^ x4 ^ y2
    print(f"{x1_x4_y2=:016b}")
    print(f"pr[x1 ^ x4 ^ y2 = 0] = {pr(x1_x4_y2, 0)}")
    print(f"pr[x1 ^ x4 ^ y2 = 1] = {pr(x1_x4_y2, 1)}")
    print(f"eps[x1 ^ x4 ^ y2 = 0] = {eps(x1_x4_y2, 0)}")
    print(f"eps[x1 ^ x4 ^ y2 = 1] = {eps(x1_x4_y2, 1)}\n")

    x3_x4_y1_y4 = x3 ^ x4 ^ y1 ^ y4
    print(f"{x3_x4_y1_y4=:016b}")
    print(f"pr[x3 ^ x4 ^ y1 ^ y4 = 0] = {pr(x3_x4_y1_y4, 0)}")
    print(f"pr[x3 ^ x4 ^ y1 ^ y4 = 1] = {pr(x3_x4_y1_y4, 1)}")
    print(f"eps[x3 ^ x4 ^ y1 ^ y4 = 0] = {eps(x3_x4_y1_y4, 0)}")
    print(f"eps[x3 ^ x4 ^ y1 ^ y4 = 1] = {eps(x3_x4_y1_y4, 1)}\n")

def main():
    zad1()

if __name__ == '__main__':
    main()
