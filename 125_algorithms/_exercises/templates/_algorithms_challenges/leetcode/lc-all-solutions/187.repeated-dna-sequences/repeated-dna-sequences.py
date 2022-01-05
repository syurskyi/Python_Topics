c_ Solution(object):
  ___ findRepeatedDnaSequences  s):
    """
    :type s: str
    :rtype: List[str]
    """
    d    # dict
    ans    # list
    ___ i __ r..(l..(s) - 9):
      key = s[i:i + 10]
      __ key __ d:
        d[key] += 1
        __ d[key] __ 2:
          ans.a..(key)
      ____:
        d[key] = 1
    r.. ans
