c_ Solution(o..
  ___ findStrobogrammatic  n
    """
    :type n: int
    :rtype: List[str]
    """
    d {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    ___ dfs(half, p.., res, n
      __ l..(p..) __ half:
        pathStr "".j..(p..)
        __ half * 2 __ n:
          res.a..(pathStr + "".j..([d[x] ___ x __ pathStr[::-1]]
        ____
          ___ c __ "018":
            res.a..(pathStr + c + "".j..([d[x] ___ x __ pathStr[::-1]]
        r..

      ___ c __ "01689":
        __ c __ "0" a.. l..(p..) __ 0:
          _____
        p...a..(c)
        dfs(half, p.., res, n)
        p...p.. )

    res    # list
    dfs(n / 2, [], res, n)
    r.. res
