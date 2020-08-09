class Solution(object
  ___ canPermutePalindrome(self, s
    """
    :type s: str
    :rtype: bool
    """
    evenCount = 0
    oddCount = 0
    d = {}
    ___ c in s:
      d[c] = d.get(c, 0) + 1
    ___ k in d:
      __ d[k] % 2 __ 1:
        oddCount += 1
      ____
        evenCount += 1

    __ le.(s) % 2 __ 1:
      __ oddCount __ 1:
        r_ True
    ____
      __ oddCount __ 0:
        r_ True
    r_ False
