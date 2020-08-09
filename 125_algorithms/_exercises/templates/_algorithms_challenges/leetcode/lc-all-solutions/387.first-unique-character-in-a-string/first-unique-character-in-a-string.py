class Solution(object
  ___ firstUniqChar(self, s
    """
    :type s: str
    :rtype: int
    """
    letters = [0] * 26
    ___ c in s:
      ci = ord(c) - ord('a')
      letters[ci] += 1
    ___ i in range(0, le.(s)):
      ci = ord(s[i]) - ord('a')
      __ letters[ci] __ 1:
        r_ i
    r_ -1
