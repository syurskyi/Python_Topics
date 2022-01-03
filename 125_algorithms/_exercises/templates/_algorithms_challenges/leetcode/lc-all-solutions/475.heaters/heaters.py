c_ Solution(object):
  ___ findRadius(self, houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    minDist = 0
    heaters.s..()
    ___ house __ s..(houses):
      idx = bisect.bisect_left(heaters, house)
      dist = float("inf")
      __ idx > 0:
        dist = m..(dist, abs(house - heaters[idx - 1]))
      __ idx < l..(heaters) - 1:
        dist = m..(dist, abs(house - heaters[idx + 1]))
      __ idx < l..(heaters):
        dist = m..(dist, abs(house - heaters[idx]))
      minDist = max(minDist, dist)
    r.. minDist
