c_ Solution(object):
  ___ lengthOfLongestSubstringKDistinct  s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    j = 0
    ans = 0
    d..    # dict
    ___ i __ r..(l..(s)):
      d..[s[i]] = d...get(s[i], 0) + 1
      w.... j <= i a.. l..(d..) > k:
        d..[s[j]] -= 1
        __ d..[s[j]] __ 0:
          del d..[s[j]]
        j += 1
      ans = m..(ans, i - j + 1)
    r.. ans
