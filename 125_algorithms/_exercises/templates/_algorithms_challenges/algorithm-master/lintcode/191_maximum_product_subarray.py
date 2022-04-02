"""
since the fact:
    the minimum negative number * -1 -> the maximum
    the maximum positive number -> the maximum
so we need record the minimum and the maximum number for each child in nums
"""


c_ Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    ___ maxProduct  A
        __ n.. A:
            r.. 0

        ans = Pmin = Pmax = A[0]
        ___ i __ r..(1, l..(A)):
            """
            adding `A[i]` to reset `min` and `max`
            if its so lowest or highest
            """
            C = (A[i], Pmin * A[i], Pmax * A[i])
            Pmin, Pmax = m..(C), m..(C)

            __ Pmax > ans:
                ans = Pmax

        r.. ans
