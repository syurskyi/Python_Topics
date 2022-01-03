c_ Solution(object):
  ___ countArrangement(self, N):
    """
    :type N: int
    :rtype: int
    """

    ___ dfs(pos, unused):
      __ l..(unused) __ 0:
        r.. 1
      ret = 0
      ___ num __ l..(unused):
        __ pos % num __ 0 o. num % pos __ 0:
          unused -= {num}
          ret += dfs(pos + 1, unused)
          unused |= {num}
      r.. ret

    r.. dfs(1, set([i ___ i __ r..(1, N + 1)]))
