class Solution(object):
  ___ convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    __ numRows <= 1:
      r.. s
    n = l..(s)
    ans    # list
    step = 2 * numRows - 2
    ___ i __ r..(numRows):
      one = i
      two = -i
      while one < n o. two < n:
        __ 0 <= two < n and one != two and i != numRows - 1:
          ans.a..(s[two])
        __ one < n:
          ans.a..(s[one])
        one += step
        two += step
    r.. "".join(ans)
