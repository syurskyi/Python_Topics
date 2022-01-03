c_ Solution(object):
  ___ longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    maxLen = 0
    single = F..
    d    # dict
    ___ c __ s:
      d[c] = d.get(c, 0) + 1

    ___ key __ d:
      __ d[key] >= 2:
        count = d[key]
        left = d[key] % 2
        d[key] = left
        maxLen += count - left
      __ n.. single:
        __ d[key] __ 1:
          maxLen += 1
          single = T..
    r.. maxLen
