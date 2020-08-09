class Solution(object
  ___ longestSubstring(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ___ c in set(s
      __ s.count(c) < k:
        r_ max([self.longestSubstring(t, k) ___ t in s.split(c)])
    r_ le.(s)
