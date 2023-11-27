# Aleksander Kluczka

from Crypto.Hash import SHA1


def chunker(sequence, chunk_size: int):
    return (
        sequence[pos : pos + chunk_size] for pos in range(0, len(sequence), chunk_size)
    )


def b2x_str(bit_str: str) -> str:
    hex_str = ""
    for c in chunker(bit_str, 8):
        hex_str += f"{int(c, 2):02X} "
    return hex_str


def sha1(message: str, print_debugs: bool = False):
    def left_rotate(number: int, rotation_count: int, number_of_bits: int = 32) -> int:
        def ensure_correct_1_bit_count() -> None:
            assert (lft := f"{number:0{number_of_bits}b}".count("1")) == (
                rgt := f"{result:0{number_of_bits}b}".count("1")
            ), f"Incorrect number of bits: {lft=} != {rgt=}"

        ### option 1 - definition from PDF, but it's not a correct bit rotation???
        ### (ASSERT FAILS)
        # print(f"org_number: {number:0{number_of_bits}b}")
        # print(
        #     f"first_part: {(number << rotation_count) & 0xFFFFFFFF:0{number_of_bits}b}"
        # )
        # print(f"secnd_part: {(number >> number_of_bits):0{number_of_bits}b}")
        # print(
        #     f"lft_rotate: {((number << rotation_count) | (number >> number_of_bits)) & 0xFFFFFFFF:032b}\n"
        # )
        # result: int = (
        #     ((number << rotation_count) & 0xFFFFFFFF) | (number >> number_of_bits)
        # ) & 0xFFFFFFFF

        ### option 2 - technically correct definition from PDF - actual rotation
        ### (same result as option 3)
        result: int = (
            ((number << rotation_count) & 0xFFFFFFFF)
            | (number >> (number_of_bits - rotation_count))
        ) & 0xFFFFFFFF

        ### option 3 - "the pythonic way"
        # number_str = f"{number:0{number_of_bits}b}"
        # result: int = int(number_str[rotation_count:] + number_str[:rotation_count], 2)

        # assert that the number of '1' is the same after rotation
        ensure_correct_1_bit_count()
        return result

    # initial variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # convert message to bits
    bit_msg = ""
    for c in message:
        bit_msg += f"{ord(c):08b}"
        # bit_msg += f"{int(c, 16):08b}"

    if print_debugs:
        print(f"msg converted to binary (in hex) = {b2x_str(bit_msg)}")

    bit_msg_length_before_fill: int = len(bit_msg)

    # start with appending '1' to the message
    bit_msg += "1"

    # append k '0' bits, where 0 <= k < 512, so that the resulting message length is congruent to
    # 448 modulo 512
    k = -1
    while True:
        k += 1
        if ((bit_msg_length_before_fill + 1 + k) % 512) == 448:
            break

    if print_debugs:
        print(f"{k=}")

    bit_msg += "0" * k
    if print_debugs:
        print(f"msg with filled 0 bits = {b2x_str(bit_msg)}")
    assert len(bit_msg) % 512 == 448

    # append length of the message as 64-bit big-endian integer
    bit_msg += f"{bit_msg_length_before_fill:064b}"
    if print_debugs:
        print(f"msg with appended length = {b2x_str(bit_msg)}")
    assert len(bit_msg) % 512 == 0

    # loop over the message in 512-bit chunks
    for chunk in chunker(bit_msg, 512):
        assert len(chunk) == 512

        # split the chunk into 16 32-bit words
        w: dict[int, str] = {}
        for i, word in enumerate(chunker(chunk, 32)):
            assert 0 <= i <= 15
            assert len(word) == 32
            w[i] = int(word, 2)
            assert 0 <= w[i] < 2**32

        # extend the first 16 words into 80 32-bit words
        for i in range(16, 80):
            w[i] = left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)
            assert 0 <= w[i] < 2**32

        a, b, c, d, e = h0, h1, h2, h3, h4

        # funny little loop
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            # some swap shenanigans
            temp = (left_rotate(a, 5) + f + e + k + w[i]) % (2**32)
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

            assert 0 <= a < (2**32)
            assert 0 <= b < (2**32)
            assert 0 <= c < (2**32)
            assert 0 <= d < (2**32)
            assert 0 <= e < (2**32)

            assert 0 <= h0 < (2**32)
            assert 0 <= h1 < (2**32)
            assert 0 <= h2 < (2**32)
            assert 0 <= h3 < (2**32)
            assert 0 <= h4 < (2**32)

        # rotate add 32-bit temp words
        h0 = (h0 + a) % (2**32)
        h1 = (h1 + b) % (2**32)
        h2 = (h2 + c) % (2**32)
        h3 = (h3 + d) % (2**32)
        h4 = (h4 + e) % (2**32)

        result = f"{h0:032b}{h1:032b}{h2:032b}{h3:032b}{h4:032b}"
        assert len(result) == (32 * 5)
        print(f"final result = {b2x_str(result)}")


def zad3(text: str):
    h = SHA1.new()
    h.update(text.encode("utf-8"))
    result = f"{int(h.hexdigest(), 16):0b}"
    print(f"Crypto.SHA1  = {b2x_str(result)}")


def zad5():
    message = ""
    print(f"message = '{message}'")

    sha1(message, print_debugs=False)
    zad3(message)


def main():
    zad5()


if __name__ == "__main__":
    main()
