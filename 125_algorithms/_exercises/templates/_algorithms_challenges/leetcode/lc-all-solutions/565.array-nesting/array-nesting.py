c_ Solution(o..
  ___ arrayNesting  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    cache [0] * l..(nums)
    ans 0
    ___ i, start __ e..(nums
      __ cache[i]:
        _____
      p start
      length 1
      w.... nums[p] != start:
        cache[nums[p]] 1
        p nums[p]
        length += 1
      ans m..(ans, length)
    r.. ans
