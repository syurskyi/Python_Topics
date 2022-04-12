c_ Excel(o..
  ___ - , H, W
    """
    :type H: int
    :type W: str
    """
    H, W decodeCoord(H, W)
    data [[0] * (W + 1) ___ _ __ r..(H + 1)]
    formulas    # dict

  ___ decodeCoord  r, c
    r.. i..(r) - 1, o..(c) - o..("A") + 1

  ___ s..  r, c, v
    """
    :type r: int
    :type c: str
    :type v: int
    :rtype: void
    """
    r, c decodeCoord(r, c)
    __ (r, c) __ formulas:
      del formulas[(r, c)]
    data[r][c] v

  ___ get  r, c
    """
    :type r: int
    :type c: str
    :rtype: int
    """
    r, c decodeCoord(r, c)
    __ (r, c) __ formulas:
      r.. computeFormula(formulas[(r, c)])
    r.. data[r][c]

  ___ computeFormula  strs
    ans 0
    ___ s __ strs:
      startI, startJ, endI, endJ parseRange(s)
      ___ i __ r..(startI, endI + 1
        ___ j __ r..(startJ, endJ + 1
          __ (i, j) __ formulas:
            ans += computeFormula(formulas[(i, j)])
          ____
            ans += data[i][j]
    r.. ans

  ___ parseRange  s
    start end s
    __ ":" __ s:
      start, end s.s..(":")
    startI, startJ decodeCoord(start[1:], start 0
    endI, endJ decodeCoord(end[1:], end 0
    r.. (startI, startJ, endI, endJ)

  ___ s..  r, c, strs
    """
    :type r: int
    :type c: str
    :type strs: List[str]
    :rtype: int
    """
    r, c decodeCoord(r, c)
    formulas[(r, c)] strs
    r.. computeFormula(strs)

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
