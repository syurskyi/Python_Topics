#/usr/bin/env python3


import sys
import sieve


def test_manual():

    primes = list(sieve.sieve_of_eratosthenes(30))
    print(primes)
    print('Should be [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]')


def test_assert_ok():

    primes = list(sieve.sieve_of_eratosthenes(30))
    assert(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


def test_assert_fail():

    primes = list(sieve.sieve_of_eratosthenes(30))
    assert(primes == [2, 3, 5, 7, 11, 13, 17, 19, 23])


def main():

    option = int(sys.argv[1])

    if option == 1:
        print('Manual Test:')
        test_manual()

    elif option == 2:
        print('Assert Test OK:')
        print('- has no output -')
        test_assert_ok()

    elif option == 3:
        print('Assert Test FAIL:')
        test_assert_fail()


if __name__ == "__main__":
    main()
