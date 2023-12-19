# Aleksander Kluczka

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from PIL import Image


def zad1():
    mods = [
        ["ecb", modes.ECB()],
        ["cbc", modes.CBC(os.urandom(16))],
        ["ctr", modes.CTR(os.urandom(16))],
    ]

    for mod_name, mod in mods:
        key = os.urandom(16)
        ecb_cipher = Cipher(algorithms.AES(key), mod)

        ecb_encryptor = ecb_cipher.encryptor()

        with Image.open("./data/Tux.ppm") as source_image:
            data = source_image.tobytes()

            size = source_image.size
            mode = source_image.mode

        padder = PKCS7(16).padder()
        data = padder.update(data) + padder.finalize()

        ecb_ciphertext = ecb_encryptor.update(data) + ecb_encryptor.finalize()

        ecb_image = Image.frombytes(mode, size, ecb_ciphertext)
        ecb_image.save(f"Tux_{mod_name}.png")


def main():
    zad1()


if __name__ == "__main__":
    main()
