import random


def miller_rabin_prime_test(n, a=None):
    if a is None:
        a = random.randint(1, n - 1)

    d = last_d = int(1)
    binary = [int(c) for c in bin(n - 1)[2:]]
    print("Binary representation of n - 1 = %d is %s" % (n - 1, binary))
    print("Initialize d and dd to 1")
    print("Starting prime test with a = %d" % a)
    counter = 0
    for b in binary:
        counter += 1
        print("Iteration %d" % counter)
        d = d * d % n
        print("Calculate %d * %d mod %d = %d" % (last_d, last_d, n, d))
        print("Is %d a square root of %d mod %d and not 1 or -1 (%d)?" % (last_d, d, n, n - 1))
        if d == 1 and last_d != 1 and last_d != n - 1:
            print("Yes. %d is definitely no prime number" % n)
            return False
        print("No, continuing...")
        if b == 1:
            print("Square and multiply: %d * %d mod %d = %d" % (d, a, n, d * a % n))
            d = d * a % n

        last_d = d

    print("After last iteration d has the value %d" % d)
    if d == 1:
        print("Since %d is 1, %d is most likely a prime number" % (d, n))
        return True
    else:
        print("Since %d is not 1, %d is definitely not a prime number" % (d, n))


def main():
    print(miller_rabin_prime_test(n=65, a=8))
    print("-----------------------------")
    print(miller_rabin_prime_test(n=65, a=12))


if __name__ == '__main__':
    main()
