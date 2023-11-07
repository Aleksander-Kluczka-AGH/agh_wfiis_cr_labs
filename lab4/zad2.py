import math

def zad2():
    P = ['a', 'b', 'c']
    C = [1, 2, 3, 4]
    K = ["K1", "K2", "K3"]

    Pr_P = {'a': 1.0/2.0, 'b': 1.0/3.0, 'c': 1.0/6.0}
    Pr_K = {'K1': 1.0/3.0, 'K2': 1.0/3.0, 'K3': 1.0/3.0}
    Pr_C = {
        1: (Pr_P['a'] * Pr_K['K1']) + (Pr_P['c'] * Pr_K['K3']),
        2: (Pr_P['a'] * Pr_K['K2']) + (Pr_P['b'] * Pr_K['K1']),
        3: (Pr_P['a'] * Pr_K['K3']) + (Pr_P['b'] * Pr_K['K2']) + (Pr_P['c'] * Pr_K['K1']),
        4: (Pr_P['b'] * Pr_K['K3']) + (Pr_P['c'] * Pr_K['K2'])
    }

    def H(target):
        sum = 0
        for k, v in target.items():
            if v == 0:
                continue
            sum += v * math.log2(v)
        return -sum

    def HH(target, req):
        sum = 0
        for r in req:
            for k, v in target.items():
                if v == 0:
                    continue
                sum += r * v * math.log2(v)
        return -sum

    H_P = H(Pr_P)
    print(f"{H_P=}")

    H_C = H(Pr_C)
    print(f"{H_C=}")

    H_K = H(Pr_K)
    print(f"{H_K=}")

    H_KC = H_K + H_P - H_C
    print(f"{H_KC=}")

    Pr_PC = {
        'a1': (Pr_P['a'] * Pr_K['K1']) / Pr_C[1],
        'a2': (Pr_P['a'] * Pr_K['K2']) / Pr_C[2],
        'a3': (Pr_P['a'] * Pr_K['K3']) / Pr_C[3],
        'a4': (Pr_P['a'] * 0) / Pr_C[4],
        'b1': (Pr_P['b'] * 0) / Pr_C[1],
        'b2': (Pr_P['b'] * Pr_K['K1']) / Pr_C[2],
        'b3': (Pr_P['b'] * Pr_K['K2']) / Pr_C[3],
        'b4': (Pr_P['b'] * Pr_K['K3']) / Pr_C[4],
        'c1': (Pr_P['c'] * Pr_K['K3']) / Pr_C[1],
        'c2': (Pr_P['c'] * 0) / Pr_C[2],
        'c3': (Pr_P['c'] * Pr_K['K1']) / Pr_C[3],
        'c4': (Pr_P['c'] * Pr_K['K2']) / Pr_C[4],
    }

    H_PC = HH(Pr_PC, Pr_C)
    print(f"{H_PC=}")



def main():
    zad2()

if __name__ == '__main__':
    main()
