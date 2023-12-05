# Aleksander Kluczka

from Crypto.Hash import SHAKE128


def zad2():
    def print_results(text):
        print(f"SHAKE-128({text}):")
        h = SHAKE128.new()
        h.update(text.encode("utf-8"))
        print(f"{h.read(256 // 8).hex()}")
        print()

    print_results("The quick brown fox jumps over the lazy dog")
    print_results("The quick brown fox jumps over the lazy dof")


def main():
    zad2()


if __name__ == "__main__":
    main()
