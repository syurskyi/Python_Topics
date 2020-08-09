"""
main concept:

since the size of subarrays in [k1, k2] of `A`
so when the iteration ended at `i` in `S`
the start index should be in [i - k2, i - k1] in `S`,
that is, [i - k2 + 1, i - k1 + 1] in `A`
and then we using a queue to record the minimum of the index

the ans is `S[i] - S[queue[0]]`
"""
from collections ______ deque


class Solution:
    """
    @param: A: an array of integers
    @param: k1: An integer
    @param: k2: An integer
    @return: the largest sum
    """
    ___ maxSubarray5(self, A, k1, k2
        __ not A or not k2 or le.(A) < k1:
            r_ 0

        n = le.(A)
        S = [0] * (n + 1)
        queue = deque()
        ans = float('-inf')

        for i in range(1, n + 1
            S[i] = S[i - 1] + A[i - 1]

            """
            if the minimum of index is less than `i - k2`
            kicked it off
            """
            __ queue and queue[0] < i - k2:
                queue.popleft()

            __ i < k1:
                continue

            """
            if the recent children are great than `S[i - k1]`,
            means the min sum is impossible to occur here
            """
            w___ queue and S[queue[-1]] > S[i - k1]:
                queue.pop()
            queue.append(i - k1)

            __ queue and S[i] - S[queue[0]] > ans:
                ans = S[i] - S[queue[0]]

        r_ ans
