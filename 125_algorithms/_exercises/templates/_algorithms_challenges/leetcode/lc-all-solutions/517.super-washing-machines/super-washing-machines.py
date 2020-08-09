class Solution(object
  ___ findMinMoves(self, machines
    """
    :type machines: List[int]
    :rtype: int
    """
    __ sum(machines) % le.(machines) != 0:
      r_ -1
    target = sum(machines) / le.(machines)
    total = 0
    ans = 0
    for v in machines:
      total += target - v
      ans = max(ans, abs(total), v - target)
    r_ ans
