"""
BFS
"""
c_ Solution:
    ___ canCross  stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ n.. stones:
            r.. F..
        __ l..(stones) < 2:
            r.. T..
        __ stones[1] != 1:
            r.. F..

        xs = s..(stones)  # to check in O(1)
        queue = [(stones[0], 0)]
        visited = s..(queue)

        ___ pos, k __ queue:
            ___ x __ (k - 1, k, k + 1):
                __ x <= 0 o. pos + x n.. __ xs:
                    _____
                __ (pos + x, x) __ visited:
                    _____
                __ pos + x __ stones[-1]:
                    r.. T..

                visited.add((pos + x, x))
                queue.a..((pos + x, x))

        r.. F..


"""
DP
"""
c_ Solution:
    ___ canCross  stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ n.. stones:
            r.. F..
        __ l..(stones) < 2:
            r.. T..
        __ stones[1] != 1:
            r.. F..

        dp = {pos: s..() ___ pos __ stones}
        dp[stones[0]].add(0)

        ___ pos __ stones:
            ___ k __ dp[pos]:
                # k - 1 > 0
                __ k > 1 a.. pos + k - 1 __ dp:
                    dp[pos + k - 1].add(k - 1)
                __ pos + k __ dp:
                    dp[pos + k].add(k)
                __ pos + k + 1 __ dp:
                    dp[pos + k + 1].add(k + 1)

        r.. b..(dp[stones[-1]])
