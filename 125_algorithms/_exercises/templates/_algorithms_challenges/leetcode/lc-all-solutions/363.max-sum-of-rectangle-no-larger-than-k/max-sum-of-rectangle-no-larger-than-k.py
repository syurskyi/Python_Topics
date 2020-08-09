______ bisect


class Solution(object
  ___ maxSumSubmatrix(self, matrix, k
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    ans = float("-inf")
    dp = [[0] * le.(matrix[0]) ___ _ in range(le.(matrix))]
    ___ i in range(0, le.(matrix)):
      ___ j in range(0, le.(matrix[0])):
        dp[i][j] = dp[i][j - 1] + matrix[i][j]
    ___ start in range(0, le.(matrix[0])):
      ___ end in range(start, le.(matrix[0])):
        sums = [0]
        subsum = 0
        ___ i in range(0, le.(matrix)):
          __ start > 0:
            subsum += dp[i][end] - dp[i][start - 1]
          ____
            subsum += dp[i][end]
          idx = bisect.bisect_left(sums, subsum - k)
          __ idx < le.(sums
            ans = max(ans, subsum - sums[idx])
          bisect.insort(sums, subsum)
    r_ ans
