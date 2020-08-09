class Solution(object
  ___ findMinMoves(self, machines
    """
    :type machines: List[int]
    :rtype: int
    """
    __ su.(machines) % le.(machines) != 0:
      r_ -1
    target = su.(machines) / le.(machines)
    total = 0
    ans = 0
    ___ v in machines:
      total += target - v
      ans = max(ans, abs(total), v - target)
    r_ ans
