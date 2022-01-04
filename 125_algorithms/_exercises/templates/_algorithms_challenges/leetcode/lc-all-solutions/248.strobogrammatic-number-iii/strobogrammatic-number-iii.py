c_ Solution(object):
  ___ findStrobogrammatic(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, n):
      __ l..(path) __ half:
        pathStr = "".j..(path)
        __ half * 2 __ n:
          toAppend = pathStr + "".j..([d[x] ___ x __ pathStr[::-1]])
          toAppendInt = i..(toAppend)
          __ low <= toAppendInt <= high:
            count += 1
        ____:
          ___ c __ "018":
            toAppend = pathStr + c + "".j..([d[x] ___ x __ pathStr[::-1]])
            toAppendInt = i..(toAppend)
            __ low <= toAppendInt <= high:
              count += 1
        r..

      ___ c __ "01689":
        __ c __ "0" a.. l..(path) __ 0:
          _____
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
    __ i..(low) > i..(high):
      r.. 0
    count = 0
    low = i..(low)
    high = i..(high)
    ___ length __ r..(l..(low), l..(high) + 1):
      findStrobogrammatic(length)
    r.. count
