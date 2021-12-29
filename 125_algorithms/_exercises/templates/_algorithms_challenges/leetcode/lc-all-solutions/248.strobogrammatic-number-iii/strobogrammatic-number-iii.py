class Solution(object):
  ___ findStrobogrammatic(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    self.d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, n):
      __ l..(path) __ half:
        pathStr = "".join(path)
        __ half * 2 __ n:
          toAppend = pathStr + "".join([self.d[x] ___ x __ pathStr[::-1]])
          toAppendInt = int(toAppend)
          __ self.low <= toAppendInt <= self.high:
            self.count += 1
        ____:
          ___ c __ "018":
            toAppend = pathStr + c + "".join([self.d[x] ___ x __ pathStr[::-1]])
            toAppendInt = int(toAppend)
            __ self.low <= toAppendInt <= self.high:
              self.count += 1
        r..

      ___ c __ "01689":
        __ c __ "0" and l..(path) __ 0:
          continue
        path.a..(c)
        dfs(half, path, n)
        path.pop()

    res    # list
    dfs(n / 2, [], n)
    r.. res

  ___ strobogrammaticInRange(self, low, high):
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    __ int(low) > int(high):
      r.. 0
    self.count = 0
    self.low = int(low)
    self.high = int(high)
    ___ length __ r..(l..(low), l..(high) + 1):
      self.findStrobogrammatic(length)
    r.. self.count
