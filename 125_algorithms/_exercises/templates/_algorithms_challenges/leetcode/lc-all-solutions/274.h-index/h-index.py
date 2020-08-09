class Solution(object
  ___ hIndex(self, citations
    """
    :type citations: List[int]
    :rtype: int
    """
    n = le.(citations)
    dp = [0] * (n + 1)
    for c in citations:
      __ c > n:
        dp[n] += 1
      ____
        dp[c] += 1

    total = 0
    for i in reversed(range(1, le.(dp))):
      total += dp[i]
      __ total >= i:
        r_ i
    r_ 0
