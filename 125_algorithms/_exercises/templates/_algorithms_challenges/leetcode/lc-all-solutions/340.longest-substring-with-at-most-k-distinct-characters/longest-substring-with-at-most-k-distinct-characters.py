c_ Solution(o..
  ___ lengthOfLongestSubstringKDistinct  s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    j = 0
    ans = 0
    d..    # dict
    ___ i __ r..(l..(s:
      d..[s[i]] = d...g.. s[i], 0) + 1
      w.... j <_ i a.. l..(d..) > k:
        d..[s[j]] -_ 1
        __ d..[s[j]] __ 0:
          del d..[s[j]]
        j += 1
      ans = m..(ans, i - j + 1)
    r.. ans
