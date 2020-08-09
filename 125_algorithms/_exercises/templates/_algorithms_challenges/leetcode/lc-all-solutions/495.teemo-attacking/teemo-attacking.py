class Solution(object
  ___ findPoisonedDuration(self, timeSeries, duration
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    __ not timeSeries:
      r_ 0
    ans = 0
    start = timeSeries[0]
    end = start + duration
    ___ i in range(1, le.(timeSeries)):
      s = timeSeries[i]
      __ s <= end:
        end = s + duration
      ____
        ans += end - start
        start = s
        end = start + duration
    ans += end - start
    r_ ans
