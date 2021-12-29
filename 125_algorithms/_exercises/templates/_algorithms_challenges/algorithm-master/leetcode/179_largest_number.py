"""
REF: https://leetcode.com/articles/largest-number/
"""


class LgSort(str):
    ___ __lt__(a, b):
        r.. a + b > b + a


class Solution:
    ___ largestNumber(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A = ''.join(s..(map(str, A), key=LgSort))
        r.. '0' __ A[0] __ '0' ____ A
