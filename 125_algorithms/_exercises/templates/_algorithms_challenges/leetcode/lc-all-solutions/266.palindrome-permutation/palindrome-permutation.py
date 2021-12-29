class Solution(object):
  ___ canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    evenCount = 0
    oddCount = 0
    d = {}
    ___ c __ s:
      d[c] = d.get(c, 0) + 1
    ___ k __ d:
      __ d[k] % 2 __ 1:
        oddCount += 1
      ____:
        evenCount += 1

    __ l..(s) % 2 __ 1:
      __ oddCount __ 1:
        r.. True
    ____:
      __ oddCount __ 0:
        r.. True
    r.. False
