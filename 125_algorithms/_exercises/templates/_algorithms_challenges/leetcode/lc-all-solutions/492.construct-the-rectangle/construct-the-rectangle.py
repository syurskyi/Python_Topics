c_ Solution(object):
  ___ constructRectangle(self, area):
    """
    :type area: int
    :rtype: List[int]
    """
    root = int(area ** 0.5)
    w.... root > 0:
      __ area % root __ 0:
        r.. int(area / root), root
      root -= 1
