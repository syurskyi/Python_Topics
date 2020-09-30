"""
BFS
"""
class Solution:
    ___ canCross(self, stones
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ not stones:
            r_ False
        __ le.(stones) < 2:
            r_ True
        __ stones[1] != 1:
            r_ False

        xs = set(stones)  # to check in O(1)
        queue = [(stones[0], 0)]
        visited = set(queue)

        ___ pos, k __ queue:
            ___ x __ (k - 1, k, k + 1
                __ x <= 0 or pos + x not __ xs:
                    continue
                __ (pos + x, x) __ visited:
                    continue
                __ pos + x __ stones[-1]:
                    r_ True

                visited.add((pos + x, x))
                queue.append((pos + x, x))

        r_ False


"""
DP
"""
class Solution:
    ___ canCross(self, stones
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ not stones:
            r_ False
        __ le.(stones) < 2:
            r_ True
        __ stones[1] != 1:
            r_ False

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

        r_ bool(dp[stones[-1]])
