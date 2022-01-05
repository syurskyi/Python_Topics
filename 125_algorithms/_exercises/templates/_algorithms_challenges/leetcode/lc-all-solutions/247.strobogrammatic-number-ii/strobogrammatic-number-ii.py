c_ Solution(object):
  ___ findStrobogrammatic  n):
    """
    :type n: int
    :rtype: List[str]
    """
    d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, path, res, n):
      __ l..(path) __ half:
        pathStr = "".j..(path)
        __ half * 2 __ n:
          res.a..(pathStr + "".j..([d[x] ___ x __ pathStr[::-1]]))
        ____:
          ___ c __ "018":
            res.a..(pathStr + c + "".j..([d[x] ___ x __ pathStr[::-1]]))
        r..

      ___ c __ "01689":
        __ c __ "0" a.. l..(path) __ 0:
          _____
        path.a..(c)
        dfs(half, path, res, n)
        path.pop()

    res    # list
    dfs(n / 2, [], res, n)
    r.. res
