class Solution(object):
  ___ lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    j = 0
    ans = 0
    d.. = {}
    ___ i __ r..(l..(s)):
      d..[s[i]] = d...get(s[i], 0) + 1
      while j <= i and l..(d..) > k:
        d..[s[j]] -= 1
        __ d..[s[j]] __ 0:
          del d..[s[j]]
        j += 1
      ans = max(ans, i - j + 1)
    r.. ans
