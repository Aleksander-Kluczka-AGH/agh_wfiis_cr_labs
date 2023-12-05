# Aleksander Kluczka

from Crypto.Hash import SHA3_224, SHA3_256, SHA3_384, SHA3_512, SHAKE128, SHAKE256


def zad1():
    def print_results(text, func, name):
        print(f"Function: {name}")
        h = func.new()
        h.update(text.encode("utf-8"))
        print(f"'{text}' -> {h.hexdigest()}")
        print()

    def print_results2(text, func, arg: int, name):
        print(f"Function: {name}")
        h = func.new()
        h.update(text.encode("utf-8"))
        print(f"'{text}' -> {h.read(arg).hex()}")
        print()

    print_results("", SHA3_224, "sha-3-224")
    print_results("", SHA3_256, "sha-3-256")
    print_results("", SHA3_384, "sha-3-384")
    print_results("", SHA3_512, "sha-3-512")
    print_results2("", SHAKE128, 256 // 8, "shake-128(256)")
    print_results2("", SHAKE128, 512 // 8, "shake-128(512)")
    print_results2("", SHAKE256, 512 // 8, "shake-256(512)")


def main():
    zad1()


if __name__ == "__main__":
    main()
