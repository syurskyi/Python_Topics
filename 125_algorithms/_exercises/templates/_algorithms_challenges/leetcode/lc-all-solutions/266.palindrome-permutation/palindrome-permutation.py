class Solution(object):
  ___ canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    evenCount = 0
    oddCount = 0
    d = {}
    for c in s:
      d[c] = d.get(c, 0) + 1
    for k in d:
      __ d[k] % 2 == 1:
        oddCount += 1
      else:
        evenCount += 1

    __ len(s) % 2 == 1:
      __ oddCount == 1:
        return True
    else:
      __ oddCount == 0:
        return True
    return False
