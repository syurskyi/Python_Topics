class Solution(object):
  ___ numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    # idea:
    # we compute the distance starting from any given point and we use a hashtable to count the number of the same distance obtained
    # once we finish counting distance for one point, we calculate the combinations = 1 * C^1_N * C^1_(N-1)
    ans = 0
    ___ p1 __ points:
      d = {}
      ___ p2 __ points:
        __ p1 != p2:
          dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
          d[dist] = d.get(dist, 0) + 1
      ___ k __ d:
        ans += d[k] * (d[k] - 1)
    r.. ans
