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

def zad1():
    y_prim_counts = {i : 0 for i in range(16)}

    x_prim = 0b1011
    print("      x |   x* |    y |   y* |   y'")
    for x in range(16):
        x_star = x ^ x_prim
        y = sbox[x]
        y_star = sbox[x_star]
        y_prim = y ^ y_star
        print(f"{x:X}: {x:04b} | {x_star:04b} | {y:04b} | {y_star:04b} | {y_prim:04b}")

        y_prim_counts[y_prim] += 1

    print()
    for i in range(16):
        print(f"{i:04b} ", end="")
    print()
    for i in range(16):
        print(f"{y_prim_counts[i]:4} ", end="")

def main():
    zad1()

if __name__ == '__main__':
    main()
