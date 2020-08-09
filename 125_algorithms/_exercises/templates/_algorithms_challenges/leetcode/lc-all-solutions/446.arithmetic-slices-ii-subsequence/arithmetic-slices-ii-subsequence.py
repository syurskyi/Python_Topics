class Solution(object
  ___ numberOfArithmeticSlices(self, A
    """
    :type A: List[int]
    :rtype: int
    """
    ans = 0
    dp = [collections.defaultdict(int) ___ _ in A]
    ___ i in range(le.(A)):
      ___ j in range(i
        diff = A[i] - A[j]
        dp[i][diff] += 1
        __ diff in dp[j]:
          dp[i][diff] += dp[j][diff]
          ans += dp[j][diff]
    r_ ans
