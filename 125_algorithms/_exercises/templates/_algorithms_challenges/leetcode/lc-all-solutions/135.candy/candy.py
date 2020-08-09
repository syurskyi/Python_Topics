class Solution(object
  ___ candy(self, ratings
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = le.(ratings)
    left = [1] * n
    ans = 0
    for i in range(1, n
      __ ratings[i] > ratings[i - 1]:
        left[i] = left[i - 1] + 1
    ans = left[-1]
    for i in reversed(range(0, n - 1)):
      __ ratings[i] > ratings[i + 1]:
        left[i] = max(left[i], left[i + 1] + 1)
      ans += left[i]
    r_ ans
