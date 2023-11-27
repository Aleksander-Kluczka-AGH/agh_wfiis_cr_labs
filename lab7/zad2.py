# Aleksander Kluczka

sbox = {
    0x0: 0xE,
    0x1: 0x4,
    0x2: 0xD,
    0x3: 0x1,
    0x4: 0x2,
    0x5: 0xF,
    0x6: 0xB,
    0x7: 0x8,
    0x8: 0x3,
    0x9: 0xA,
    0xA: 0x6,
    0xB: 0xC,
    0xC: 0x5,
    0xD: 0x9,
    0xE: 0x0,
    0xF: 0x7
}

def N_d(x_prim, sbox) -> dict[int, int]:
    y_prim_counts = {i : 0 for i in range(16)}

    for x in range(16):
        x_star = x ^ x_prim
        y = sbox[x]
        y_star = sbox[x_star]
        y_prim = y ^ y_star

        y_prim_counts[y_prim] += 1

    return y_prim_counts

def zad2():
    print("a'\\b'", end="")
    for i in range(16):
        print(f"{i:2X} ", end="")
    print()
    print("-" * 54)
    for a_prim in range(16):
        print(f"{a_prim:2} | ", end="")

        nd = N_d(a_prim, sbox)
        for i in range(16):
            print(f"{nd[i]:2} ", end="")
        print()


def main():
    zad2()

if __name__ == '__main__':
    main()
