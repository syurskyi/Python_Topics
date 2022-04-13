c_ Solution(o..
  ___ nearestPalindromic  n
    """
    :type n: str
    :rtype: str
    """
    l l..(n)
    cands s..([s..(10 ** l + 1), s..(10 ** (l - 1) - 1)])
    prefix i..(n[:(l + 1) / 2])
    ___ half __ m.. s.., [prefix - 1, prefix, prefix + 1]
      cands.add(half + [half, half[:-1]][l & 1][::-1])
    cands.discard(n)
    r.. m..(cands, k.._l.... x: (a..(i..(x) - i..(n, i..(x)))
