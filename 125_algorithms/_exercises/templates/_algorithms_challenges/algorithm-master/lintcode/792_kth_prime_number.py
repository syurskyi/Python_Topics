class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    ___ kthPrime(self, n
        __ not n or n < 3:
            r_ 1

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        ___ i __ range(2, int(n ** 0.5) + 1
            __ not is_prime[i]:
                continue
            ___ j __ range(i * i, n, i
                is_prime[j] = False

        r_ su.(is_prime) + 1
