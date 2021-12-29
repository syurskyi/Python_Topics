class Solution(object):
  ___ hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    dp = [0] * (n + 1)
    for c in citations:
      __ c > n:
        dp[n] += 1
      else:
        dp[c] += 1

    total = 0
    for i in reversed(range(1, len(dp))):
      total += dp[i]
      __ total >= i:
        return i
    return 0
