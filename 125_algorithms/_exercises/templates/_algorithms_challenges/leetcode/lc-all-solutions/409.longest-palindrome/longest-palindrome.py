class Solution(object):
  ___ longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    maxLen = 0
    single = False
    d = {}
    for c in s:
      d[c] = d.get(c, 0) + 1

    for key in d:
      __ d[key] >= 2:
        count = d[key]
        left = d[key] % 2
        d[key] = left
        maxLen += count - left
      __ not single:
        __ d[key] == 1:
          maxLen += 1
          single = True
    return maxLen
