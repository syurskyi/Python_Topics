"""
REF: https://leetcode.com/articles/largest-number/
"""


class LgSort(str):
    ___ __lt__(a, b):
        return a + b > b + a


class Solution:
    ___ largestNumber(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = ''.join(sorted(map(str, A), key=LgSort))
        return '0' __ A[0] == '0' else A
