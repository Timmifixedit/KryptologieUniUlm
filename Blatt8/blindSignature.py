def ext_ggt(a, b):
    if b == 0:
        return a, 1, 0

    d, x, y = ext_ggt(b, a % b)
    return d, y, x - (a // b) * y


def calc_inverse(a, n):
    _, _, y = ext_ggt(n, a)
    return y


def main():
    n = 119
    e = 11
    m = 9
    z = 3

    m_tilde = z**e * m % n
    print("a): Calculate ~m = z^e * m mod n = %d^%d mod %d = %d" % (z, e, n, m_tilde))
    print()
    print("b): Calculate ~u = ~m^d mod")
    print("First calculate d as the inverse of e mod phi(n)")
    phi_n = 16 * 6
    print("phi(n) = %d * %d = %d" % (16, 6, phi_n))
    d = calc_inverse(e, phi_n)
    print("The inverse to %d mod %d is %d = d" % (e, phi_n, d))
    u_tilde = m_tilde**d % n
    print("Therefor ~u = %d^%d mod %d = %d" % (m_tilde, d, n, u_tilde))
    print()
    print("c) Multiply ~u with the inverse of z to get u")
    z_inverse = calc_inverse(z, n)
    print("z' = %d" % z_inverse)
    u = u_tilde * z_inverse % n
    print("u = %d * %d mod %d = %d" % (u_tilde, z_inverse, n, u))
    print("Verify blind signature: u has to be equal to m^d mod n")
    u_ver = m**d % n
    print("%d^%d mod %d = %d" % (m, d, n, u_ver))


if __name__ == '__main__':
    main()

