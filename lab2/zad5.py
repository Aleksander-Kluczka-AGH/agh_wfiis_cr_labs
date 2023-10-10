import random

def crypt(letter, key):
    return chr((ord(letter) - ord('a') + key) % 26 + ord('a'))

def zad5():
    results = []
    for i in range(1000):
        random_length = random.randint(5, 100)
        random_key = random.randint(0, 25)

        random_plaintext = ''.join([chr(random.randint(0, 25) + ord('a')) for _ in range(random_length)])
        encrypted = ''.join([crypt(c, random_key) for c in random_plaintext])

        for i in range(1, 26):
            decrypted = ''.join([crypt(c, -i) for c in encrypted])

            if decrypted == random_plaintext:
                results.append(i)
                break

    print(f"average key: {sum(results) / len(results)}")


def main():
    zad5()

if __name__ == '__main__':
    main()
