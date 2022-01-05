"""
Premium question
"""
__author__ = 'Daniel'


c_ Solution(o..):
    ___ getModifiedArray  length, updates):
        """
        Brute force: O(kn)

        Algorithm: Complement
        [i, j] increases by delta is equivalent to [i, n) increase delta and [j+1, n) decreases by delta; thus we only
        need to update two positions O(1) rather than update the entire range [i, j] in O(n)

        ...++++....
        ...++++++++
        .......----

        Complexity: O(k + n)

        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        deltas = [0 ___ _ __ x..(length)]
        ___ i, j, k __ updates:
            deltas[i] += k
            __ j + 1 < length: deltas[j + 1] -= k

        ret    # list
        acc = 0
        ___ delta __ deltas:
            acc += delta
            ret.a..(acc)

        r.. ret
