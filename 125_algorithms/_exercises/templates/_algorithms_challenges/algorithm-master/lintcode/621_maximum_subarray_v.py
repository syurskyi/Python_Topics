"""
main concept:

since the size of subarrays in [k1, k2] of `A`
so when the iteration ended at `i` in `S`
the start index should be in [i - k2, i - k1] in `S`,
that is, [i - k2 + 1, i - k1 + 1] in `A`
and then we using a queue to record the minimum of the index

the ans is `S[i] - S[queue[0]]`
"""
____ c.. _______ d..


c_ Solution:
    """
    @param: A: an array of integers
    @param: k1: An integer
    @param: k2: An integer
    @return: the largest sum
    """
    ___ maxSubarray5  A, k1, k2
        __ n.. A o. n.. k2 o. l..(A) < k1:
            r.. 0

        n = l..(A)
        S = [0] * (n + 1)
        queue = d..()
        ans = f__('-inf')

        ___ i __ r..(1, n + 1
            S[i] = S[i - 1] + A[i - 1]

            """
            if the minimum of index is less than `i - k2`
            kicked it off
            """
            __ queue a.. queue[0] < i - k2:
                queue.popleft()

            __ i < k1:
                _____

            """
            if the recent children are great than `S[i - k1]`,
            means the min sum is impossible to occur here
            """
            w.... queue a.. S[queue[-1]] > S[i - k1]:
                queue.p.. )
            queue.a..(i - k1)

            __ queue a.. S[i] - S[queue[0]] > ans:
                ans = S[i] - S[queue[0]]

        r.. ans
