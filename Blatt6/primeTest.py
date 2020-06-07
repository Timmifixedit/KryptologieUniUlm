import random
import sys


def miller_rabin_prime_test(n, a=None, verbose=False):
    if a is None:
        a = random.randint(1, n - 1)

    d = last_d = int(1)
    binary = [int(c) for c in bin(n - 1)[2:]]
    if verbose:
        print("Binary representation of n - 1 = %d is %s" % (n - 1, binary))
        print("Initialize d and dd to 1")
        print("Starting prime test with a = %d" % a)

    counter = 0
    for b in binary:
        counter += 1
        if verbose:
            print("Iteration %d" % counter)

        d = d * d % n
        if verbose:
            print("Calculate %d * %d mod %d = %d" % (last_d, last_d, n, d))
            print("Is %d a square root of 1 mod %d and not 1 or -1 (%d)?" % (last_d, n, n - 1))

        if d == 1 and last_d != 1 and last_d != n - 1:
            if verbose:
                print("Yes. %d is definitely no prime number" % n)

            return False

        if verbose:
            print("No, continuing...")

        if b == 1:
            if verbose:
                print("Square and multiply: %d * %d mod %d = %d" % (d, a, n, d * a % n))

            d = d * a % n

        last_d = d
    if verbose:
        print("After last iteration d has the value %d" % d)

    if d == 1:
        if verbose:
            print("Since %d is 1, %d is most likely a prime number" % (d, n))

        return True
    elif verbose:
        print("Since %d is not 1, %d is definitely not a prime number" % (d, n))

    return False


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print(miller_rabin_prime_test(n))
    else:
        print(miller_rabin_prime_test(n=65, a=8, verbose=True))
        print("-----------------------------")
        print(miller_rabin_prime_test(n=65, a=12, verbose=True))


if __name__ == '__main__':
    main()
