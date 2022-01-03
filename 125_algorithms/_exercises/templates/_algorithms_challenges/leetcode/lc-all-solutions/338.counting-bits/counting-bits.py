c_ Solution(object):
  ___ countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    __ num __ 0:
      r.. [0]
    ans = [0, 1]
    j = 0
    ___ i __ r..(2, num + 1):
      ans.a..(ans[i & (i - 1)] + 1)
    r.. ans
