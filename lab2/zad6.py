import numpy as np

def crypt(letter_num, key):
    return (letter_num + key) % 26

def zad6():
    cypher = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
    key_frequency_table = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    print(f"cypher: {cypher}")
    print(f"frequency_table: {key_frequency_table}")

    cypher_frequency_table = []
    for i in range(26):
        cypher_frequency_table.append(cypher.count(chr(i + ord('A'))))

    argmax = np.argmax(cypher_frequency_table)

    print(f"Most common letter: {chr(argmax + ord('A'))} with {cypher_frequency_table[argmax]} instances")

    cypher_num = [ord(c) - ord('A') for c in cypher]
    for letter in key_frequency_table:
        key =  (argmax - (ord(letter) - ord('A'))) % 26
        plaintext = ''.join([chr(crypt(c, -key) + ord('a')) for c in cypher_num])
        print(f"Potential key: {key} -> {plaintext}")


def main():
    zad6()

if __name__ == '__main__':
    main()
