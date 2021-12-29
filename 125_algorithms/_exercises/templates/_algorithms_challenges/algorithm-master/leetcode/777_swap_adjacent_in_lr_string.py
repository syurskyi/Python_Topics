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

        w.... i < m a.. j < n:
            w.... i < m a.. start[i] __ 'X':
                i += 1
            w.... j < n a.. end[j] __ 'X':
                j += 1

            __ i __ m a.. j __ n:
                r.. True
            __ i __ m o. j __ n:
                r.. False

            __ start[i] != end[j]:
                r.. False
            __ start[i] __ 'L' a.. j > i:
                r.. False
            __ start[i] __ 'R' a.. i > j:
                r.. False

            i += 1
            j += 1

        r.. True
