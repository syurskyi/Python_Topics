class Solution(object
  ___ canCross(self, stones
    """
    :type stones: List[int]
    :rtype: bool
    """
    dp = {}

    ___ dfs(stones, pos, k
      key = pos + k * 10000;
      __ dp.has_key(key
        r_ dp[key]
      ____
        for i in range(pos + 1, le.(stones)):
          step = stones[i] - stones[pos]
          __ step < k - 1:
            continue;
          __ step > k + 1:
            dp[key] = False
            r_ False
          __ dfs(stones, i, step
            dp[key] = True
            r_ True
      dp[key] = (pos __ le.(stones) - 1)
      r_ (pos __ le.(stones) - 1)

    r_ dfs(stones, 0, 0)
