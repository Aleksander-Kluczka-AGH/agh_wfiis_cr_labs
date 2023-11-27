# Aleksander Kluczka

import numpy as np

def SPN(x, sbox, pbox, key):

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


    for r in range(1, N-1):
        u[r] = w[r-1] ^ k[r]
        v[r] = 0
        for i in range(4):
            v[r] |= (sbox[(u[r] >> i*4) & 0xF] << i*4)

        w[r] = pbox(v[r])

    u[N-1] = w[N-2] ^ k[N-1]
    v[N-1] = 0
    for i in range(4):
        v[N-1] |= (sbox[(u[N-1] >> i*4) & 0xF] << i*4)

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

rsbox = {v: k for k, v in sbox.items()}

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

sbox_str = {f"{k:04b}": f"{v:04b}" for k, v in sbox.items()}

def differential_attack():
    def get_quartet(xy, index):
        index -= 1
        xy_str = f"{xy:016b}"
        quartet_str = xy_str[index*4:index*4+4]
        quartet = int(quartet_str, 2)
        return quartet

    count_L1_L2 = np.array([0] * 16 * 16).reshape(16, 16)

    x_prim = 0b0000101100000000
    for x in range(0, 120):
        y = SPN(x, sbox, pbox, 0b00111010100101001101011000111111)
        x_star = x ^ x_prim
        y_star = SPN(x_star, sbox, pbox, 0b00111010100101001101011000111111)

        if (get_quartet(y, 1) == get_quartet(y_star, 1)) and (get_quartet(y, 3) == get_quartet(y_star, 3)):
            for L1 in range(0, 16):
                for L2 in range(0, 16):
                    v4_2 = L1 ^ get_quartet(y, 2)
                    v4_4 = L2 ^ get_quartet(y, 4)
                    u4_2 = rsbox[v4_2]
                    u4_4 = rsbox[v4_4]

                    v4_2_star = L1 ^ get_quartet(y_star, 2)
                    v4_4_star = L2 ^ get_quartet(y_star, 4)
                    u4_2_star = rsbox[v4_2_star]
                    u4_4_star = rsbox[v4_4_star]

                    u4_2_prim = u4_2 ^ u4_2_star
                    u4_4_prim = u4_4 ^ u4_4_star

                    if u4_2_prim == 0b0110 and u4_4_prim == 0b0110:
                        count_L1_L2[L1][L2] += 1

    max = -1
    max_key = [0, 0]
    for L1 in range(0, 16):
        for L2 in range(0, 16):
            if count_L1_L2[L1][L2] > max:
                max = count_L1_L2[L1][L2]
                max_key = [L1, L2]

    print(f"max_key[L1, L2] = [{max_key[0]}, {max_key[1]}]")
    print(f"K5: xxxx {max_key[0]:04b} xxxx {max_key[1]:04b}")



def zad3():
    differential_attack()


def main():
    zad3()

if __name__ == '__main__':
    main()
