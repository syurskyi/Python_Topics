class Solution(object):
  ___ reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    return " ".join(s.split()[::-1])
