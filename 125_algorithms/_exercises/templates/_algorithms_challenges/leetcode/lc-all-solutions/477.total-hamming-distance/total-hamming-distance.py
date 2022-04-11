c_ Solution(o..
  ___ totalHammingDistance  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    ans 0
    mask 1
    ___ j __ r..(0, 32
      ones zeros 0
      ___ num __ nums:
        __ num & mask:
          ones += 1
        ____
          zeros += 1
      ans += ones * zeros
      mask mask << 1
    r.. ans
