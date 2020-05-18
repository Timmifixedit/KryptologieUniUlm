alpha = 0
beta = 1
gamma = 2
delta = 3

circ_op = [
    [alpha, beta, gamma, delta],
    [beta, alpha, delta, gamma],
    [gamma, delta, alpha, beta],
    [delta, gamma, beta, alpha]
]


def q_index(num):
    sq = num // 16
    q = (num // 4) % 4
    o = num % 4
    return sq, q, o


def main():
    num_permutations = 4**3
    for i in range(num_permutations):
        a, b, c = q_index(i)
        print("a: %d, b: %d, c: %d" % (a, b, c))
        print(circ_op[a]   [circ_op[b][c]] == circ_op[circ_op[a][b]]   [c])



if __name__ == "__main__":
    main()