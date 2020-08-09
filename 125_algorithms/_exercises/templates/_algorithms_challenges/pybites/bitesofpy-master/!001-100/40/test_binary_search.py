from string ______ ascii_lowercase

from binary_search ______ binary_search

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)


___ test_binary_search_prime(
    assert binary_search(PRIMES, 2) __ 0
    assert binary_search(PRIMES, 59) __ 16
    assert binary_search(PRIMES, 5) __ 2
    assert binary_search(PRIMES, 61) __ 17
    assert binary_search(PRIMES, 18) __ None


___ test_binary_search_alpha(
    assert binary_search(ALPHABET, 'u') __ 20
    assert binary_search(ALPHABET, 'a') __ 0
    assert binary_search(ALPHABET, 'z') __ 25