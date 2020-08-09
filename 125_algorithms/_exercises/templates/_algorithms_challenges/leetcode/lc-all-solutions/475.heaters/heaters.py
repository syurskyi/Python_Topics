class Solution(object
  ___ findRadius(self, houses, heaters
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    minDist = 0
    heaters.sort()
    ___ house in sorted(houses
      idx = bisect.bisect_left(heaters, house)
      dist = float("inf")
      __ idx > 0:
        dist = min(dist, abs(house - heaters[idx - 1]))
      __ idx < le.(heaters) - 1:
        dist = min(dist, abs(house - heaters[idx + 1]))
      __ idx < le.(heaters
        dist = min(dist, abs(house - heaters[idx]))
      minDist = max(minDist, dist)
    r_ minDist
