class Solution(object):
  ___ maxRotateFunction(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    __ n.. A:
      r.. 0

    sumA = s..(A)
    fk = 0
    n = l..(A)
    ___ i, num __ enumerate(A):
      fk += i * num
    idx = n - 1
    ans = float("-inf")
    ___ _ __ r..(n):
      fk += sumA - n * A[idx]
      ans = max(ans, fk)
      idx -= 1
    r.. ans
