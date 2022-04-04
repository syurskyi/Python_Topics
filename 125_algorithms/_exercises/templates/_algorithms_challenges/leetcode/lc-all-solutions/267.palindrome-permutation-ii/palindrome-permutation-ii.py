_______ c..


c_ Solution(o..
  ___ generatePalindromes  s
    """
    :type s: str
    :rtype: List[str]
    """

    ___ helper(s, p.., ans, visited
      __ l..(p..) __ l..(s
        ans.a..("".j..(p..
        r..

      ___ i __ r..(l..(s:
        __ i > 0 a.. s[i] __ s[i - 1] a.. i - 1 n.. __ visited o. i __ visited:
          _____
        visited |= {i}
        p...a..(s[i])
        helper(s, p.., ans, visited)
        p...pop()
        visited -= {i}

    ans    # list
    res    # list
    ss = ""
    mid = ""
    counter = c...C..(s)
    oddChars = f.. l.... x: counter[x] % 2 __ 1, counter)
    __ l..(s) % 2 __ 1:
      __ l..(oddChars) __ 1:
        mid = oddChars[0]
        counter[mid] -= 1
      ____:
        r.. []
    ____ l..(oddChars) > 0:
      r.. []

    ___ key __ counter:
      ss += key * (counter[key] / 2)

    helper(s..(ss), [], res, s..
    ___ hword __ res:
      ans.a..(hword + mid + hword[::-1])
    r.. ans
