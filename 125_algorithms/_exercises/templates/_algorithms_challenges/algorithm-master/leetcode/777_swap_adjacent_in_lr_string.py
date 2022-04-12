c_ Solution:
    ___ canTransform  start, end
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        __ l..(start) !_ l..(end
            r.. F..

        m, n l..(start), l..(end)
        i j 0

        w.... i < m a.. j < n:
            w.... i < m a.. start[i] __ 'X':
                i += 1
            w.... j < n a.. end[j] __ 'X':
                j += 1

            __ i __ m a.. j __ n:
                r.. T..
            __ i __ m o. j __ n:
                r.. F..

            __ start[i] !_ end[j]:
                r.. F..
            __ start[i] __ 'L' a.. j > i:
                r.. F..
            __ start[i] __ 'R' a.. i > j:
                r.. F..

            i += 1
            j += 1

        r.. T..
