def add_z26(a, b):
    return (a + b) % 26

def zad1():
    plaintext = "thiscryptosystemisnotsecure"
    key = "CIPHER"
    print("key: " + key)

    def get_next_key_char(index):
        return key[index % len(key)]

    print("Encryption")
    output = ""
    for index, c in enumerate(plaintext):
        text_as_num = ord(c) - ord('a')
        key_as_num = ord(get_next_key_char(index)) - ord('A')

        output += chr(add_z26(text_as_num, key_as_num) + ord('A'))

    print("Plaintext: " + plaintext)
    print("Cyphertext: " + output)

    print("\nDecryption")
    output2 = ""
    for index, c in enumerate(output):
        text_as_num = ord(c) - ord('A')
        key_as_num = ord(get_next_key_char(index)) - ord('A')

        output2 += chr(((text_as_num - key_as_num) % 26) + ord('a'))

    print("Plaintext: " + output)
    print("Cyphertext: " + output2)


def main():
    zad1()

if __name__ == '__main__':
    main()
