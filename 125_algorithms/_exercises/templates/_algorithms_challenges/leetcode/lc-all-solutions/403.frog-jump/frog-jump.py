c_ Solution(o..):
  ___ canCross  stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    dp    # dict

    ___ dfs(stones, pos, k):
      key = pos + k * 10000;
      __ dp.has_key(key):
        r.. dp[key]
      ____:
        ___ i __ r..(pos + 1, l..(stones)):
          step = stones[i] - stones[pos]
          __ step < k - 1:
            _____;
          __ step > k + 1:
            dp[key] = F..
            r.. F..
          __ dfs(stones, i, step):
            dp[key] = T..
            r.. T..
      dp[key] = (pos __ l..(stones) - 1)
      r.. (pos __ l..(stones) - 1)

    r.. dfs(stones, 0, 0)
