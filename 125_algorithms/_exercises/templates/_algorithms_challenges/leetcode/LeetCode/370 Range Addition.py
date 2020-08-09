"""
Premium question
"""
__author__ = 'Daniel'


class Solution(object
    ___ getModifiedArray(self, length, updates
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
        deltas = [0 ___ _ in xrange(length)]
        ___ i, j, k in updates:
            deltas[i] += k
            __ j + 1 < length: deltas[j + 1] -= k

        ret = []
        acc = 0
        ___ delta in deltas:
            acc += delta
            ret.append(acc)

        r_ ret
