c_ Solution:
    ___ nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: list[int]
        :rtype: int
        """
        __ n.. n o. n <= 1 o. n.. primes:
            r.. 1

        k = l..(primes)

        # i -> same as `i` in `primes`, v -> track of how far `primes[i]` stay in `uglys`
        steps = [0] * k
        uglys = [0] * n
        uglys[0] = 1

        ___ i __ r..(1, n):
            ugly = float('inf')

            ___ j __ r..(k):
                ugly = m..(ugly, uglys[steps[j]] * primes[j])

            uglys[i] = ugly

            ___ j __ r..(k):
                __ uglys[steps[j]] * primes[j] __ ugly:
                    steps[j] += 1

        r.. uglys[n - 1]
