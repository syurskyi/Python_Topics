c_ Solution(o..
  ___ singleNumber  nums
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    ___ num __ nums:
      xor ^= num

    xor = xor & -xor
    a, b = 0, 0
    ___ num __ nums:
      __ num & xor:
        a ^= num
      ____
        b ^= num

    r.. a, b
