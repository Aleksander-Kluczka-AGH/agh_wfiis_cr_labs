def zad4():
    cypher = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
    outputs = [""] * 26

    for i in range(1, 26):
        outputs[i] = ''.join([chr((ord(c) - ord('A') + i) % 26 + ord('a')) for c in cypher])
        print(f"{i}: {outputs[i]}")

    print(f"plaintext: {outputs[10]}")

def main():
    zad4()

if __name__ == '__main__':
    main()
