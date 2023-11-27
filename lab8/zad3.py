# Aleksander Kluczka

from Crypto.Hash import MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA512

def zad3():
    texts = [
        "The quick brown fox jumps over the lazy dog",
        "The quick brown fox jumps over the lazy cog",
        "",
    ]

    def print_results(texts, func, name):
        print(f"Function: {name}")
        for text in texts:
            h = func.new()
            h.update(text.encode('utf-8'))
            print(f"'{text}' -> {h.hexdigest()}")
        print()

    print_results(texts, MD4, "md4")
    print_results(texts, MD5, "md5")
    print_results(texts, SHA1, "sha1")
    print_results(texts, SHA224, "sha224")
    print_results(texts, SHA256, "sha256")
    print_results(texts, SHA384, "sha384")
    print_results(texts, SHA512, "sha512")


def main():
    zad3()

if __name__ == '__main__':
    main()
