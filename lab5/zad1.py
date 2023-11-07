def SPN(x, sbox, pbox, key):
    print(f"Key: {key:032b}\n")

    k = [
        0,
        (key & 0xFFFF0000) >> 16,
        (key & 0x0FFFF000) >> 12,
        (key & 0x00FFFF00) >> 8,
        (key & 0x000FFFF0) >> 4,
        (key & 0x0000FFFF),
    ]
    N = len(k) - 1
    u: dict[int, int] = {}
    v: dict[int, int] = {}
    w: dict[int, int] = {0: x}

    print(f"x : {x:016b}\n")
    print(f"w0: {w[0]:016b}\n")

    for r in range(1, N-1):
        print(f"K{r}: {k[r]:016b}")

        u[r] = w[r-1] ^ k[r]
        print(f"u{r}: {u[r]:016b}")

        v[r] = 0
        for i in range(4):
            v[r] |= (sbox[(u[r] >> i*4) & 0xF] << i*4)
        print(f"v{r}: {v[r]:016b}")

        w[r] = pbox(v[r])
        print(f"w{r}: {w[r]:016b}\n")

    u[N-1] = w[N-2] ^ k[N-1]
    v[N-1] = 0
    for i in range(4):
        v[N-1] |= (sbox[(u[N-1] >> i*4) & 0xF] << i*4)

    print(f"K4: {k[N-1]:016b}")
    print(f"u4: {u[N-1]:016b}")
    print(f"v4: {v[N-1]:016b}\n")

    print(f"K5: {k[N]:016b}\n")

    y = v[N-1] ^ k[N]

    return y

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

def pbox(v):
    w = 0
    w |= ((v >> 15) & 1) << 15
    w |= ((v >> 11) & 1) << 14
    w |= ((v >> 7) & 1) << 13
    w |= ((v >> 3) & 1) << 12
    w |= ((v >> 14) & 1) << 11
    w |= ((v >> 10) & 1) << 10
    w |= ((v >> 6) & 1) << 9
    w |= ((v >> 2) & 1) << 8
    w |= ((v >> 13) & 1) << 7
    w |= ((v >> 9) & 1) << 6
    w |= ((v >> 5) & 1) << 5
    w |= ((v >> 1) & 1) << 4
    w |= ((v >> 12) & 1) << 3
    w |= ((v >> 8) & 1) << 2
    w |= ((v >> 4) & 1) << 1
    w |= ((v >> 0) & 1) << 0
    return w

def zad1():
    # 0011 1010 1001 0100 1101 0110 0011 1111
    key = 0b00111010100101001101011000111111

    # 0010 0110 1011 0111
    x = 0b0010011010110111

    # Encryption
    y = SPN(x, sbox, pbox, key)
    print(f"y : {y:016b}\n\n")


def main():
    zad1()

if __name__ == '__main__':
    main()
