class Solution(object
  ___ findStrobogrammatic(self, n
    """
    :type n: int
    :rtype: List[str]
    """
    self.d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, n
      __ le.(path) __ half:
        pathStr = "".join(path)
        __ half * 2 __ n:
          toAppend = pathStr + "".join([self.d[x] for x in pathStr[::-1]])
          toAppendInt = int(toAppend)
          __ self.low <= toAppendInt <= self.high:
            self.count += 1
        ____
          for c in "018":
            toAppend = pathStr + c + "".join([self.d[x] for x in pathStr[::-1]])
            toAppendInt = int(toAppend)
            __ self.low <= toAppendInt <= self.high:
              self.count += 1
        r_

      for c in "01689":
        __ c __ "0" and le.(path) __ 0:
          continue
        path.append(c)
        dfs(half, path, n)
        path.pop()

    res = []
    dfs(n / 2, [], n)
    r_ res

  ___ strobogrammaticInRange(self, low, high
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    __ int(low) > int(high
      r_ 0
    self.count = 0
    self.low = int(low)
    self.high = int(high)
    for length in range(le.(low), le.(high) + 1
      self.findStrobogrammatic(length)
    r_ self.count
