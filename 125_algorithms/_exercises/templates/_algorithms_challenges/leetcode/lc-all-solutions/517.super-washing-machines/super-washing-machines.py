class Solution(object):
  ___ findMinMoves(self, machines):
    """
    :type machines: List[int]
    :rtype: int
    """
    __ sum(machines) % len(machines) != 0:
      return -1
    target = sum(machines) / len(machines)
    total = 0
    ans = 0
    for v in machines:
      total += target - v
      ans = max(ans, abs(total), v - target)
    return ans
