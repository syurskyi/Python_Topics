c_ Solution(o..
  ___ isAnagram  s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    __ n.. l..(s) __ l..(t
      r.. F..

    sHash tHash 1
    sCount [0] * 26
    tCount [0] * 26
    p1 2903
    p2 29947
    ___ i __ r..(0, l..(s:
      sCount[o..(s[i]) - o..('a')] += 1
      tCount[o..(t[i]) - o..('a')] += 1

    ___ i __ r..(0, 26
      sHash sHash * p1 + sCount[i]
      tHash tHash * p1 + tCount[i]
      p1 *= p2
    r.. sHash __ tHash
