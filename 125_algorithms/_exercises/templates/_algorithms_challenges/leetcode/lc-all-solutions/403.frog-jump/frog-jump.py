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
        r.. dp[key]
      ____:
        ___ i __ r..(pos + 1, l..(stones)):
          step = stones[i] - stones[pos]
          __ step < k - 1:
            continue;
          __ step > k + 1:
            dp[key] = False
            r.. False
          __ dfs(stones, i, step):
            dp[key] = True
            r.. True
      dp[key] = (pos __ l..(stones) - 1)
      r.. (pos __ l..(stones) - 1)

    r.. dfs(stones, 0, 0)
