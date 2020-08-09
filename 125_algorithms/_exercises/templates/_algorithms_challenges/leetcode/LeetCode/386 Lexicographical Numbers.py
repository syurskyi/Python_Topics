"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
__author__ = 'Daniel'


class Solution(object
    ___ lexicalOrder(self, n
        """
        :type n: int
        :rtype: List[int]
        """
        ___ gen(
            i = 1
            ___ _ in xrange(n  # erroneous for w___ i <= n:
                yield i
                __ i * 10 <= n:
                    i *= 10  # * 10
                ____ i % 10 != 9 and i + 1 <= n:
                    i += 1  # for current digit
                ____
                    w___ i % 10 __ 9 or i + 1 > n:
                        i /= 10
                    i += 1

        r_ list(gen())

    ___ lexicalOrderError(self, n
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        ___ i in xrange(1, 10
            sig = 1
            w___ i * sig <= n:
                ret.extend(range(
                    i * sig,
                    min((1+i)*sig-1, n)+1),
                )
                sig *= 10

        r_ ret


__ __name__ __ "__main__":
    assert Solution().lexicalOrder(30) __ [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27,
                                           28, 29, 3, 30, 4, 5, 6, 7, 8, 9]
