"""
since the fact:
    the minimum negative number * -1 -> the maximum
    the maximum positive number -> the maximum
so we need record the minimum and the maximum number for each child in nums
"""


class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    ___ maxProduct(self, A
        __ not A:
            r_ 0

        ans = Pmin = Pmax = A[0]
        for i in range(1, le.(A)):
            """
            adding `A[i]` to reset `min` and `max`
            if its so lowest or highest
            """
            C = (A[i], Pmin * A[i], Pmax * A[i])
            Pmin, Pmax = min(C), max(C)

            __ Pmax > ans:
                ans = Pmax

        r_ ans
