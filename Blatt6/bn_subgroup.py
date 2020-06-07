import sys


def calc_u(n):
    u = 1
    u_res = []
    k_res = []
    while 2**u <= n - 1:
        u_exp = 2**u
        if (n - 1) % u_exp == 0:
            k = (n - 1) // u_exp
            if k % 2 != 0:
                u_res.append(u)
                k_res.append(k)

        u += 1

    assert len(u_res) == 1
    return u_res[0], k_res[0]


def calc_b_n(u, k):
    n = 2**u * k + 1
    max_i = -1
    b_i = n - 1
    found = False
    for b in range(1, n):
        for i in range(u):
            if b**(2**i) % n == n - 1 and i > max_i:
                max_i = i
                b_i = b
                found = True

    assert found
    b_n = []
    for a in range(1, n):
        tmp = a**(k * 2**max_i) % n
        if tmp == 1 or tmp == n - 1:
            b_n.append(a)

    return b_n, max_i, b_i


def ggt(a, b):
    if a == b:
        return a
    return ggt(a - b, b) if a > b else ggt(b - a, a)


def calc_z_n_star(n):
    p_range = range(1, n, 2) if n % 2 == 0 else range(1, n)
    z_n_star = []
    for i in p_range:
        if ggt(i, n) == 1:
            z_n_star.append(i)

    return z_n_star


def main():
    n = int(sys.argv[1])
    print("n = %d" % n)
    u, k = calc_u(n)
    print("u = %d, k = %d" % (u, k))
    b_n, i, b_i = calc_b_n(u, k)
    print("Subgroup B_n")
    print(b_n)
    print("Where i = %d with corresponding b = %d" % (i, b_i))
    print("Z_n*:")
    z_n_star = calc_z_n_star(n)
    print(z_n_star)
    print("phi(%d) = %d" % (n, len(z_n_star)))
    for a in b_n:
        print("%d ^ %d = %d" % (a, k * 2**i, a**(k * 2**i) % n))


if __name__ == '__main__':
    main()
