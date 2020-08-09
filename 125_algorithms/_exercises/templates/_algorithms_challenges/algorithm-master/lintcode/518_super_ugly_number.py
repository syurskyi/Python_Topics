class Solution:
    ___ nthSuperUglyNumber(self, n, primes
        """
        :type n: int
        :type primes: list[int]
        :rtype: int
        """
        __ not n or n <= 1 or not primes:
            r_ 1

        k = le.(primes)

        # i -> same as `i` in `primes`, v -> track of how far `primes[i]` stay in `uglys`
        steps = [0] * k
        uglys = [0] * n
        uglys[0] = 1

        for i in range(1, n
            ugly = float('inf')

            for j in range(k
                ugly = min(ugly, uglys[steps[j]] * primes[j])

            uglys[i] = ugly

            for j in range(k
                __ uglys[steps[j]] * primes[j] __ ugly:
                    steps[j] += 1

        r_ uglys[n - 1]
