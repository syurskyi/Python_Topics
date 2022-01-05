c_ Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    ___ kthPrime  n):
        __ n.. n o. n < 3:
            r.. 1

        is_prime = [T..] * n
        is_prime[0] = is_prime[1] = F..

        ___ i __ r..(2, i..(n ** 0.5) + 1):
            __ n.. is_prime[i]:
                _____
            ___ j __ r..(i * i, n, i):
                is_prime[j] = F..

        r.. s..(is_prime) + 1
