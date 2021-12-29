"""
Description:

Count the number of prime numbers less than a non-negative number, n.


"""

class Solution(object):
    ___ countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [True ___ i __ r..(n)]
        i = 2
        w.... i * i < n:
            __ t[i] __ False:
                i += 1
                continue
            j = i * i
            w.... j < n:
                t[j] = False
                j += i
            i += 1
        res = 0
        ___ i __ r..(2, n):
            __ t[i] __ True:
                res += 1
        r.. res


s = Solution()
print(s.countPrimes(500))
