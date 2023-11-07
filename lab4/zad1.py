def zad1():
    def KSA(key):
        S = [i for i in range(0, 256)]
        j = 0
        for i in range(0, 256):
            j = (j+ S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def Stream_Generator(plaintext, S):
        i = 0
        j = 0
        for k in range(0, len(plaintext)):
            i = (i+1) % 256
            j = (j+S[i]) % 256
            S[i], S[j] = S[j], S[i]
            byte_key : int = S[(S[i] + S[j]) % 256]
            yield byte_key

    def encode(plaintext, keystream):
        plaintext_num = [ord(i) for i in plaintext]
        plaintext_hex = ''.join([f'{i:02X}' for i in plaintext_num])
        retval = ''
        for p, k in zip(plaintext_hex, keystream):
            retval += f'{(int(p, 16) ^ int(k, 16)):X}'
        return retval

    def RC4(plaintext, key):
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        gen = Stream_Generator(plaintext, KSA(key))
        keystream = ''.join([f'{i:02X}' for i in gen])
        print(f"Keystream: {keystream}")
        ciphertext = encode(plaintext, keystream)
        print(f"Ciphertext:{ciphertext}\n")

    RC4("Attack at dawn", "Secret")
    RC4("Plaintext", "Key")
    RC4("pedia", "Wiki")

def main():
    zad1()

if __name__ == '__main__':
    main()
