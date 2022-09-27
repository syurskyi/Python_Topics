c_ Solution o..
    ___ countPrimes  n):
        """
        :type n: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        isPrime = [T..] * n
        ___ i __ xrange(2, n):
            __ i * i >= n:
                break
            __ not isPrime[i]:
                continue
            ___ j __ xrange(i * i, n, i):
                isPrime[j] = F..
        count = 0
        ___ i __ xrange(2, n):
            __ isPrime[i]:
                count += 1
        r_ count
