class Solution(object):
  ___ longestSubstring(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    for c in set(s):
      __ s.count(c) < k:
        return max([self.longestSubstring(t, k) for t in s.split(c)])
    return len(s)
