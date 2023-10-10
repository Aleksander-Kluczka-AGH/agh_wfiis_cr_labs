def to_num(c):
    return ord(c) - ord('A')

def to_num2(c):
    return ord(c) - ord('a')

def zad3():
    plaintext = "TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
    permutation = {
        1: 2, 2: 4, 3: 6, 4: 1, 5: 8, 6: 3, 7: 5, 8: 7
    }
    inv_permutation = {v: k for k, v in permutation.items()}

    print("Decryption")
    print("Cyphertext: " + plaintext)

    plaintext_num = [to_num(c) for c in plaintext]
    plaintext_splits = [plaintext_num[i:i+8] for i in range(0, len(plaintext_num), 8)]
    output = [0] * len(plaintext_num)
    for index, split in enumerate(plaintext_splits):
        for i in range(len(split)):
            output[index*8 + i] = split[permutation[i + 1]-1]

    output_text = ''.join([chr(c + ord('a')) for c in output])
    print("Plaintext: " + output_text)

    print("Encryption")
    print("Plaintext: " + output_text)

    output_text_num = [to_num2(c) for c in output_text]
    output_text_splits = [output_text_num[i:i+8] for i in range(0, len(output_text_num), 8)]
    output2 = [0] * len(output_text_num)
    for index, split in enumerate(output_text_splits):
        for i in range(len(split)):
            output2[index*8 + i] = split[inv_permutation[i + 1]-1]

    output2_text = ''.join([chr(c + ord('A')) for c in output2])
    print("Cyphertext: " + output2_text)



def main():
    zad3()

if __name__ == '__main__':
    main()
