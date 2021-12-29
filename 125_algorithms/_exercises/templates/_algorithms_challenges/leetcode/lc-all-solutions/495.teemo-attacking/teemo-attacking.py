class Solution(object):
  ___ findPoisonedDuration(self, timeSeries, duration):
    """
    :type timeSeries: List[int]
    :type duration: int
    :rtype: int
    """
    __ not timeSeries:
      return 0
    ans = 0
    start = timeSeries[0]
    end = start + duration
    for i in range(1, len(timeSeries)):
      s = timeSeries[i]
      __ s <= end:
        end = s + duration
      else:
        ans += end - start
        start = s
        end = start + duration
    ans += end - start
    return ans
