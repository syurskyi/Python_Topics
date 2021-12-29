class Solution(object):
  ___ lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    __ len(s) == 0:
      return 0
    s = s.split()
    __ len(s) > 0:
      return len(s[-1])
    return 0
