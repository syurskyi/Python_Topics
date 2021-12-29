"""
BFS
"""
class Solution:
    ___ canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ not stones:
            return False
        __ len(stones) < 2:
            return True
        __ stones[1] != 1:
            return False

        xs = set(stones)  # to check in O(1)
        queue = [(stones[0], 0)]
        visited = set(queue)

        for pos, k in queue:
            for x in (k - 1, k, k + 1):
                __ x <= 0 or pos + x not in xs:
                    continue
                __ (pos + x, x) in visited:
                    continue
                __ pos + x == stones[-1]:
                    return True

                visited.add((pos + x, x))
                queue.append((pos + x, x))

        return False


"""
DP
"""
class Solution:
    ___ canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        __ not stones:
            return False
        __ len(stones) < 2:
            return True
        __ stones[1] != 1:
            return False

        dp = {pos: set() for pos in stones}
        dp[stones[0]].add(0)

        for pos in stones:
            for k in dp[pos]:
                # k - 1 > 0
                __ k > 1 and pos + k - 1 in dp:
                    dp[pos + k - 1].add(k - 1)
                __ pos + k in dp:
                    dp[pos + k].add(k)
                __ pos + k + 1 in dp:
                    dp[pos + k + 1].add(k + 1)

        return bool(dp[stones[-1]])
