class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    ___ kthPrime(self, n):
        __ n.. n o. n < 3:
            r.. 1

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        ___ i __ r..(2, int(n ** 0.5) + 1):
            __ n.. is_prime[i]:
                continue
            ___ j __ r..(i * i, n, i):
                is_prime[j] = False

        r.. s..(is_prime) + 1
