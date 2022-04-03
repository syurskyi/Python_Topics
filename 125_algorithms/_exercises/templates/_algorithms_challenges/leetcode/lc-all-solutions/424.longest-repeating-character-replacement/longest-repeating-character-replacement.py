____ c.. _______ d..


c_ Solution(o..
  ___ characterReplacement  s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ans  0
    d    # dict
    start  0
    maxCount  0
    window  d..([])
    ___ end __ r..(0, l..(s)):
      d[s[end]]  d.g.. s[end], 0) + 1
      maxCount  m..(maxCount, d[s[end]])
      __ end - start + 1 - maxCount > k:
        d[s[start]] - 1
        start + 1
      ans  m..(ans, end - start + 1)
    r.. ans
