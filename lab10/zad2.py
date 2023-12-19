# Aleksander Kluczka

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def zad2():
    def a():
        key = os.urandom(16)
        input = b"00000000000000000000000000000000"
        l = len(input)
        print(f"k = {key.hex()}")
        cipher = Cipher(algorithms.AES128(key), modes.ECB())

        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(input) + encryptor.finalize()
        print(f"enc({input.decode()}) = {ciphertext.hex()[:l]}")

        decryptor = cipher.decryptor()
        text = decryptor.update(ciphertext) + decryptor.finalize()
        print(f"dec({ciphertext.hex()[:l]}) = {text.decode()}")
        print()

    def b():
        key = os.urandom(16)
        input = b"0000000000000000000000000000000000000000000000000000000000000000"
        l = len(input)
        print(f"k = {key.hex()}")
        cipher = Cipher(algorithms.AES128(key), modes.ECB())

        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(input) + encryptor.finalize()
        print(
            f"enc({input[:l//2].decode()} {input[:l//2].decode()})\n=   {ciphertext.hex()[:l//2]} {ciphertext.hex()[l//2:l]}"
        )
        print()

    def c():
        key = os.urandom(16)
        iv = os.urandom(16)
        input = b"0000000000000000000000000000000000000000000000000000000000000000"
        l = len(input)
        print(f"k = {key.hex()}")

        cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(input) + encryptor.finalize()
        print(f"iv ={iv.hex()}")
        print(
            f"enc({input[:l//2].decode()} {input[:l//2].decode()})\n=   {ciphertext.hex()[:l//2]} {ciphertext.hex()[l//2:l]}"
        )

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(input) + encryptor.finalize()
        print(f"iv ={iv.hex()}")
        print(
            f"enc({input[:l//2].decode()} {input[:l//2].decode()})\n=   {ciphertext.hex()[:l//2]} {ciphertext.hex()[l//2:l]}"
        )

    a()
    b()
    c()


def main():
    zad2()


if __name__ == "__main__":
    main()
