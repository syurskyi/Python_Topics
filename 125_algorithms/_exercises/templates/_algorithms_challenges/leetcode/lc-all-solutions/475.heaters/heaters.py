c_ Solution(o..
  ___ findRadius  houses, heaters
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    minDist 0
    heaters.s..()
    ___ house __ s..(houses
      idx b__.bisect_left(heaters, house)
      dist f__("inf")
      __ idx > 0:
        dist m..(dist, a..(house - heaters[idx - 1]
      __ idx < l..(heaters) - 1:
        dist m..(dist, a..(house - heaters[idx + 1]
      __ idx < l..(heaters
        dist m..(dist, a..(house - heaters[idx]
      minDist m..(minDist, dist)
    r.. minDist
