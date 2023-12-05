# Aleksander Kluczka

from Crypto.Hash import HMAC, SHA3_256, SHA3_512, SHA256, SHA512


def zad3():
    def encrypt(text, key, func):
        h = HMAC.new(key.encode("utf-8"), digestmod=func)
        h.update(text.encode("utf-8"))
        return f"{h.hexdigest()}"

    def print_results(text, key, func, name):
        print(f'HMAC_{name}("{key}", "{text}")')
        print(f"{encrypt(text, key, func)}")
        print()

    text = "The quick brown fox jumps over the lazy dog"
    key = "key"
    print_results(text, key, SHA256, "SHA256")
    print_results(text, key, SHA3_256, "SHA3-256")
    print_results(text, key, SHA512, "SHA512")
    print_results(text, key, SHA3_512, "SHA3-512")

    print("====\n")

    msg_encoder = SHA256.new()
    msg_encoder.update(text.encode("utf-8"))
    msg = msg_encoder.hexdigest()
    print(f'Encoding message "{text}" with SHA256: ')
    print(f'"{msg}"')

    mac_encoder = HMAC.new(key.encode("utf-8"), digestmod=SHA256)
    mac_encoder.update(text.encode("utf-8"))
    mac_enc: str = mac_encoder.hexdigest()

    # msg is decoded back to text

    mac_decoder = HMAC.new(key.encode("utf-8"), digestmod=SHA256)
    mac_decoder.update(text.encode("utf-8"))

    print(f'Validating message "{msg}" with key "{key}" and mac "{mac_enc}":')

    try:
        mac_decoder.hexverify(mac_enc)
        print(f"The message '{msg}' is authentic")
    except ValueError:
        print("The message or the key is wrong")


def main():
    zad3()


if __name__ == "__main__":
    main()
