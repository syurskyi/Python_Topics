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

        ___ pos, k in queue:
            ___ x in (k - 1, k, k + 1
                __ x <= 0 or pos + x not in xs:
                    continue
                __ (pos + x, x) in visited:
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

        dp = {pos: set() ___ pos in stones}
        dp[stones[0]].add(0)

        ___ pos in stones:
            ___ k in dp[pos]:
                # k - 1 > 0
                __ k > 1 and pos + k - 1 in dp:
                    dp[pos + k - 1].add(k - 1)
                __ pos + k in dp:
                    dp[pos + k].add(k)
                __ pos + k + 1 in dp:
                    dp[pos + k + 1].add(k + 1)

        r_ bool(dp[stones[-1]])
