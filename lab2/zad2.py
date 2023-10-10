import numpy as np

def to_num(c):
    return ord(c) - ord('a')

def multi_inverse(b, n):
    r1 = n
    r2 = b
    t1 = 0
    t2 = 1

    while(r1 > 0):
        q = int(r1/r2)
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t

        if(r1 == 1):
            inv_t = t1
            break

    return inv_t

def zad2():
    plaintext = "july"
    key = np.array([[11, 8], [3, 7]])

    det = int(np.linalg.det(key))
    plaintext_num = [to_num(c) for c in plaintext]
    text_matrix = np.array(plaintext_num).reshape(2, 2)

    print(f"det = {det}")

    print("Encryption")
    print("Plaintext: " + plaintext)

    output_num = np.dot(text_matrix, key) % 26
    output = ''.join([chr(c + ord('A')) for c in output_num.flatten()])

    print("Cyphertext: " + output)

    print("\nDecryption")
    print("Plaintext: " + output)

    plaintext_num = [(ord(c) - ord('A')) for c in output]
    text_matrix = np.array(plaintext_num).reshape(2, 2)

    inv_key = np.array([[7, 18], [23, 11]])

    output_num = np.dot(text_matrix, inv_key) % 26
    output = ''.join([chr(c + ord('a')) for c in output_num.flatten()])

    print(f"Cyphertext: {output}")

def main():
    zad2()

if __name__ == '__main__':
    main()
