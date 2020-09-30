class Solution(object
  ___ minDistance(self, height, width, tree, squirrel, nuts
    """
    :type height: int
    :type width: int
    :type tree: List[int]
    :type squirrel: List[int]
    :type nuts: List[List[int]]
    :rtype: int
    """

    ___ dist(s, t
      x1, y1 = s
      x2, y2 = t
      r_ abs(x1 - x2) + abs(y1 - y2)

    ans = 0
    ___ nut __ nuts:
      ans += 2 * dist(tree, nut)

    ret = float("inf")
    ___ nut __ nuts:
      ret = min(ret, ans - dist(nut, tree) + dist(nut, squirrel))
    r_ ret
