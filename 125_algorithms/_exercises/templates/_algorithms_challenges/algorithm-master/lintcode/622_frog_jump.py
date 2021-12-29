"""
BFS
"""
class Solution:
    ___ canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ n.. stones:
            r.. False
        __ l..(stones) < 2:
            r.. True
        __ stones[1] != 1:
            r.. False

        xs = set(stones)  # to check in O(1)
        queue = [(stones[0], 0)]
        visited = set(queue)

        ___ pos, k __ queue:
            ___ x __ (k - 1, k, k + 1):
                __ x <= 0 o. pos + x n.. __ xs:
                    continue
                __ (pos + x, x) __ visited:
                    continue
                __ pos + x __ stones[-1]:
                    r.. True

                visited.add((pos + x, x))
                queue.a..((pos + x, x))

        r.. False


"""
DP
"""
class Solution:
    ___ canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ n.. stones:
            r.. False
        __ l..(stones) < 2:
            r.. True
        __ stones[1] != 1:
            r.. False

        dp = {pos: set() ___ pos __ stones}
        dp[stones[0]].add(0)

        ___ pos __ stones:
            ___ k __ dp[pos]:
                # k - 1 > 0
                __ k > 1 and pos + k - 1 __ dp:
                    dp[pos + k - 1].add(k - 1)
                __ pos + k __ dp:
                    dp[pos + k].add(k)
                __ pos + k + 1 __ dp:
                    dp[pos + k + 1].add(k + 1)

        r.. bool(dp[stones[-1]])
