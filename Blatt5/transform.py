# very naive implementation. modulus has to be prime!
def calc_inverse(number, modulus):
    return number ** (modulus - 2) % modulus


def inverse_trafo(a_vec, n_vec):
    assert len(a_vec) == len(n_vec)
    n = 1
    for n_i in n_vec:
        n *= n_i

    x = 0
    for a_i, n_i in zip(a_vec, n_vec):
        m_i = n / n_i
        x += a_i * calc_inverse(m_i, n_i) * m_i

    return int(x % n)


def main():
    w = [inverse_trafo([1, 1], [5, 11]), inverse_trafo([-1, 1], [5, 11]),
         inverse_trafo([1, -1], [5, 11]), inverse_trafo([-1, -1], [5, 11])]

    for w_i in w:
        print("Square root of 1 mod 55 is %d" % w_i)
        print("%d^2 = %d mod 55" % (w_i, w_i**2 % 55))


if __name__ == '__main__':
    main()
