class Solution(object):

  ___ repeatedSubstringPattern(self, str):
    """
    :type str: str
    :rtype: bool
    """
    for i in range(0, len(str) / 2):
      __ not len(str) % (i + 1) and str[:i + 1] * (len(str) / (i + 1)) == str:
        return True
    return False
