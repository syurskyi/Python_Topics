class Solution(object
  ___ longestSubstring(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ___ c __ set(s
      __ s.count(c) < k:
        r_ ma.([self.longestSubstring(t, k) ___ t __ s.split(c)])
    r_ le.(s)
