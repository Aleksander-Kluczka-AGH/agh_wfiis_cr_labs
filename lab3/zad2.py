from copy import copy

def zad2():
    def gen(index, start: list[int]):
        if index < 5:
            return start[index]
        else:
            temp = copy(start)
            for i in range(0, index):
                temp[i % 5] = (temp[(i % 5) - 5] + temp[(i % 5) - 2]) % 2
            return temp[index % 5]


    def generate(start: list[int], length = 50):
        return ''.join([chr(gen(i, start) + ord('0')) for i in range(0, length)])

    plaintext_str = "011001111111000"
    plaintext = [ord(c) - ord('0') for c in plaintext_str]

    stream = generate([1, 1, 0, 1, 0], length=15)

    def encode(plaintext, stream):
        return ''.join([chr(((ord(p) + ord(k)) % 2) + ord('0')) for p, k in zip(plaintext, stream)])

    print(f"Encryption:")
    print(f"Plaintext: {plaintext_str}")
    print(f"Key stream:{stream}")
    encoded = encode(plaintext_str, stream)
    print(f"Cyphertext:{encoded}")

    def decode(plaintext, stream):
        return ''.join([chr(((ord(p) - ord(k)) % 2) + ord('0')) for p, k in zip(plaintext, stream)])

    print("Decryption:")
    print(f"Cyphertext:{encoded}")
    print(f"Key stream:{stream}")
    decoded = decode(encoded, stream)
    print(f"Plaintext: {decoded}")



def main():
    zad2()

if __name__ == '__main__':
    main()
