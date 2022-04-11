c_ Solution(o..
  ___ convert  s, numRows
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    __ numRows <_ 1:
      r.. s
    n l..(s)
    ans    # list
    step 2 * numRows - 2
    ___ i __ r..(numRows
      one i
      two -i
      w.... one < n o. two < n:
        __ 0 <_ two < n a.. one != two a.. i != numRows - 1:
          ans.a..(s[two])
        __ one < n:
          ans.a..(s[one])
        one += step
        two += step
    r.. "".j..(ans)
