c_ Solution(object):
  ___ checkInclusion  s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    d    # dict
    n = l..(s1)
    ___ c __ s1:
      d[c] = d.get(c, 0) + 1
    window    # dict
    ___ i, c __ e..(s2):
      window[c] = window.get(c, 0) + 1
      __ i >= l..(s1):
        window[s2[i - n]] = window.get(s2[i - n], 0) - 1
        __ window[s2[i - n]] __ 0:
          del window[s2[i - n]]
      __ window __ d:
        r.. T..
    r.. F..
