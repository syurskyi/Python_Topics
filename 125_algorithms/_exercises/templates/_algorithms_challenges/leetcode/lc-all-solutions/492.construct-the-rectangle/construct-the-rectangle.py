class Solution(object):
  ___ constructRectangle(self, area):
    """
    :type area: int
    :rtype: List[int]
    """
    root = int(area ** 0.5)
    while root > 0:
      __ area % root == 0:
        return int(area / root), root
      root -= 1
