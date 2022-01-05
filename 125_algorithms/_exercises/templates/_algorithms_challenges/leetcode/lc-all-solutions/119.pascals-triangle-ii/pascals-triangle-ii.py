c_ Solution(object):
  ___ getRow  rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    fact = [1] * (rowIndex + 1)
    ans = [1] * (rowIndex + 1)
    ___ i __ r..(1, rowIndex + 1):
      fact[i] = fact[i - 1] * i
    ___ i __ r..(1, rowIndex):
      ans[i] = fact[-1] / (fact[i] * fact[rowIndex - i])
    r.. ans
