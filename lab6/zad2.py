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

sbox_str = {f"{k:04b}": f"{v:04b}" for k, v in sbox.items()}

def zad2():
    def pr(val) -> float:
        return val / 16.0

    def eps(val) -> float:
        return pr(val) - 0.5

    def lin_approx_table():
        for a in range(0, 16):
            a_bits = f"{a:04b}"
            for b in range(0, 16):
                b_bits = f"{b:04b}"

                N_l = 0
                for k, v in sbox_str.items():
                    xor_result = 0
                    for index, a_bit in enumerate(a_bits):
                        if a_bit == '1':
                            xor_result ^= int(k[index])
                    for index, b_bit in enumerate(b_bits):
                        if b_bit == '1':
                            xor_result ^= int(v[index])
                    xor_result ^= 0

                    if xor_result == 0:
                        N_l += 1

                print(f"{N_l:3}", end=' ')
            print()

    lin_approx_table()
    print()

    def lin_approx_table_eps():
        for a in range(0, 16):
            a_bits = f"{a:04b}"
            for b in range(0, 16):
                b_bits = f"{b:04b}"

                N_l = 0
                for k, v in sbox_str.items():
                    xor_result = 0
                    for index, a_bit in enumerate(a_bits):
                        if a_bit == '1':
                            xor_result ^= int(k[index])
                    for index, b_bit in enumerate(b_bits):
                        if b_bit == '1':
                            xor_result ^= int(v[index])
                    xor_result ^= 0

                    if xor_result == 0:
                        N_l += 1

                print(f"{eps(N_l):6}", end=' ')
            print()

    lin_approx_table_eps()

def main():
    zad2()

if __name__ == '__main__':
    main()
