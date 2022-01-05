"""
Description:

Count the number of prime numbers less than a non-negative number, n.


"""

c_ Solution(o..):
    ___ countPrimes  n):
        """
        :type n: int
        :rtype: int
        """
        t = [T.. ___ i __ r..(n)]
        i = 2
        w.... i * i < n:
            __ t[i] __ F..:
                i += 1
                _____
            j = i * i
            w.... j < n:
                t[j] = F..
                j += i
            i += 1
        res = 0
        ___ i __ r..(2, n):
            __ t[i] __ T..:
                res += 1
        r.. res


s = Solution()
print(s.countPrimes(500))
