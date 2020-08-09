class Solution(object
  ___ findMinArrowShots(self, points
    """
    :type points: List[List[int]]
    :rtype: int
    """
    ans = 0
    points.sort(key=lambda p: p[1])
    end = float("-inf")
    for s, e in points:
      __ s > end:
        ans += 1
        end = e
    r_ ans
