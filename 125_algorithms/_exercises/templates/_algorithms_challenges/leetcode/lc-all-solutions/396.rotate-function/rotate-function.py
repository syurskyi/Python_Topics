c_ Solution(o..):
  ___ maxRotateFunction  A):
    """
    :type A: List[int]
    :rtype: int
    """
    __ n.. A:
      r.. 0

    sumA = s..(A)
    fk = 0
    n = l..(A)
    ___ i, num __ e..(A):
      fk += i * num
    idx = n - 1
    ans = f__("-inf")
    ___ _ __ r..(n):
      fk += sumA - n * A[idx]
      ans = m..(ans, fk)
      idx -= 1
    r.. ans
