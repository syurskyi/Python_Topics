c_ Solution(o..
  ___ firstUniqChar  s
    """
    :type s: str
    :rtype: int
    """
    letters = [0] * 26
    ___ c __ s:
      ci = o..(c) - o..('a')
      letters[ci] += 1
    ___ i __ r..(0, l..(s:
      ci = o..(s[i]) - o..('a')
      __ letters[ci] __ 1:
        r.. i
    r.. -1
