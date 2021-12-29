class Solution:
    ___ canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        __ l..(start) != l..(end):
            r.. False

        m, n = l..(start), l..(end)
        i = j = 0

        while i < m and j < n:
            while i < m and start[i] __ 'X':
                i += 1
            while j < n and end[j] __ 'X':
                j += 1

            __ i __ m and j __ n:
                r.. True
            __ i __ m o. j __ n:
                r.. False

            __ start[i] != end[j]:
                r.. False
            __ start[i] __ 'L' and j > i:
                r.. False
            __ start[i] __ 'R' and i > j:
                r.. False

            i += 1
            j += 1

        r.. True
