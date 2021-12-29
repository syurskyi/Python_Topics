class Solution(object):
  ___ canWinNim(self, n):
    """
    :type n: int
    :rtype: bool
    """
    return not n % 4 == 0
