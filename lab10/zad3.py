# Aleksander Kluczka


def left_rotate(number: int, rotation_count: int, number_of_bits: int = 32) -> int:
    def ensure_correct_1_bit_count() -> None:
        assert (lft := f"{number:0{number_of_bits}b}".count("1")) == (
            rgt := f"{result:0{number_of_bits}b}".count("1")
        ), f"Incorrect number of bits: {lft=} != {rgt=}"

    result: int = (
        ((number << rotation_count) & 0xFFFFFFFF)
        | (number >> (number_of_bits - rotation_count))
    ) & 0xFFFFFFFF

    ensure_correct_1_bit_count()
    return result


def rotword(word: int) -> int:
    return left_rotate(word, 8, 32)


def subword(word: int) -> int:
    def subword_byte(byte: int) -> int:
        def gf_invert(byte: int, mod=0x1B) -> int:
            # https://stackoverflow.com/a/45444561/14048504
            def gf_degree(byte: int) -> int:
                result = 0
                byte >>= 1
                while byte != 0:
                    byte >>= 1
                    result += 1
                return result

            if byte == 0:
                return 0

            v = mod
            g1 = 1
            g2 = 0
            j = gf_degree(byte) - 8

            while byte != 1:
                if j < 0:
                    byte, v = v, byte
                    g1, g2 = g2, g1
                    j = -j

                byte ^= v << j
                g1 ^= g2 << j

                byte %= 256  # Emulating 8-bit overflow
                g1 %= 256  # Emulating 8-bit overflow

                j = gf_degree(byte) - gf_degree(v)

            return g1

        c = [int(i) for i in "01100011"][::-1]
        byte_rev: list[int] = [int(i) for i in f"{gf_invert(byte):08b}"][::-1]
        retval = []
        for i in range(8):
            b_i: int = (
                byte_rev[i]
                + byte_rev[(i + 4) % 8]
                + byte_rev[(i + 5) % 8]
                + byte_rev[(i + 6) % 8]
                + byte_rev[(i + 7) % 8]
                + c[i]
            ) % 2
            retval.append(str(b_i))
        retval_str = "".join(retval[::-1])
        return int(retval_str, 2)

    b0 = subword_byte((word >> 24) & 0xF)
    b1 = subword_byte((word >> 16) & 0xF)
    b2 = subword_byte((word >> 8) & 0xF)
    b3 = subword_byte((word >> 0) & 0xF)
    return (b0 << 24) | (b1 << 16) | (b2 << 8) | b3


def keyexpansion(key: str) -> str:
    def key_byte(index: int) -> int:
        return int(key[2 * index : 2 * index + 2], 16)

    rcon: list = [
        0x01000000,
        0x02000000,
        0x04000000,
        0x08000000,
        0x10000000,
        0x20000000,
        0x40000000,
        0x80000000,
        0x1B000000,
        0x36000000,
    ]
    w = {}
    for i in range(4):
        w[i] = (
            (key_byte(4 * i) << 24)
            | (key_byte(4 * i + 1) << 16)
            | (key_byte(4 * i + 2) << 8)
            | key_byte(4 * i + 3)
        )
        assert w[i] < 2**32

    for i in range(4, 44):
        temp: int = w[i - 1]
        if (i % 4) == 0:
            rotated_temp = rotword(temp)
            subworded_temp = subword(rotated_temp)
            temp = subworded_temp ^ rcon[(i // 4) - 1]
        w[i] = w[i - 4] ^ temp

    w = "".join([f"{w[i]:08x}" for i in range(44)])
    return w


def zad3():
    cipher_key = "2b7e151628aed2a6abf7158809cf4f3c"
    print(f"key = '{cipher_key}'")

    expanded_key = keyexpansion(cipher_key)
    print(f"expanded key = '{expanded_key}'")


def main():
    zad3()


if __name__ == "__main__":
    main()
