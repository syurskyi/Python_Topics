c_ Solution(o..):
  ___ plusOne  d..):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    ___ i __ r..(r..(0, l..(d..))):
      digit = (d..[i] + carry) % 10
      carry = 1 __ digit < d..[i] ____ 0
      d..[i] = digit
    __ carry __ 1:
      r.. [1] + d..
    r.. d..
