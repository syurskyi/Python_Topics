class Solution(object):
  ___ firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    letters = [0] * 26
    ___ c __ s:
      ci = ord(c) - ord('a')
      letters[ci] += 1
    ___ i __ r..(0, l..(s)):
      ci = ord(s[i]) - ord('a')
      __ letters[ci] __ 1:
        r.. i
    r.. -1
