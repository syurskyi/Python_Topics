class Solution(object):
  ___ canCross(self, stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    dp = {}

    ___ dfs(stones, pos, k):
      key = pos + k * 10000;
      __ dp.has_key(key):
        return dp[key]
      else:
        for i in range(pos + 1, len(stones)):
          step = stones[i] - stones[pos]
          __ step < k - 1:
            continue;
          __ step > k + 1:
            dp[key] = False
            return False
          __ dfs(stones, i, step):
            dp[key] = True
            return True
      dp[key] = (pos == len(stones) - 1)
      return (pos == len(stones) - 1)

    return dfs(stones, 0, 0)
