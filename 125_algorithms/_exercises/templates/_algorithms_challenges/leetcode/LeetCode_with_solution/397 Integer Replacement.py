"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ integerReplacement  n
        """
        Simulation using dp fails since bi-directional
        Simple recursion

        Math solution: bit manipulation
        https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations/
        3 is a special case
        :type n: int
        :rtype: int
        """
        ret = 0
        w.... n != 1:
            ret += 1
            __ n & 1 __ 0:
                n >>= 1
            ____ n __ 0b11 o. n >> 1 & 1 __ 0:
                n -= 1
            ____:
                n += 1

        r.. ret

    ___ integerReplacementRecur  n
        """
        Simple recursion
        :type n: int
        :rtype: int
        """
        __ n __ 1: r.. 0

        ret = 1
        __ n%2 __ 0:
            ret += integerReplacement(n/2)
        ____:
            ret += m..(integerReplacement(n+1), integerReplacement(n-1))

        r.. ret
