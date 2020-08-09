class Excel(object
  ___ __init__(self, H, W
    """
    :type H: int
    :type W: str
    """
    H, W = self.decodeCoord(H, W)
    self.data = [[0] * (W + 1) for _ in range(H + 1)]
    self.formulas = {}

  ___ decodeCoord(self, r, c
    r_ int(r) - 1, ord(c) - ord("A") + 1

  ___ set(self, r, c, v
    """
    :type r: int
    :type c: str
    :type v: int
    :rtype: void
    """
    r, c = self.decodeCoord(r, c)
    __ (r, c) in self.formulas:
      del self.formulas[(r, c)]
    self.data[r][c] = v

  ___ get(self, r, c
    """
    :type r: int
    :type c: str
    :rtype: int
    """
    r, c = self.decodeCoord(r, c)
    __ (r, c) in self.formulas:
      r_ self.computeFormula(self.formulas[(r, c)])
    r_ self.data[r][c]

  ___ computeFormula(self, strs
    ans = 0
    for s in strs:
      startI, startJ, endI, endJ = self.parseRange(s)
      for i in range(startI, endI + 1
        for j in range(startJ, endJ + 1
          __ (i, j) in self.formulas:
            ans += self.computeFormula(self.formulas[(i, j)])
          ____
            ans += self.data[i][j]
    r_ ans

  ___ parseRange(self, s
    start = end = s
    __ ":" in s:
      start, end = s.split(":")
    startI, startJ = self.decodeCoord(start[1:], start[0])
    endI, endJ = self.decodeCoord(end[1:], end[0])
    r_ (startI, startJ, endI, endJ)

  ___ sum(self, r, c, strs
    """
    :type r: int
    :type c: str
    :type strs: List[str]
    :rtype: int
    """
    r, c = self.decodeCoord(r, c)
    self.formulas[(r, c)] = strs
    r_ self.computeFormula(strs)

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
