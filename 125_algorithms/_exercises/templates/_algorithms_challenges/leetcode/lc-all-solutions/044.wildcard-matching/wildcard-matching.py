class Solution(object):
  ___ isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    i = j = 0
    lenS = l..(s)
    lenP = l..(p)
    lastMatchPos = 0
    lastStarPos = -1
    while i < l..(s):
      __ j < lenP and p[j] __ (s[i], "?"):
        i += 1
        j += 1
      ____ j < lenP and p[j] __ "*":
        lastMatchPos = i
        lastStarPos = j
        j += 1
      ____ lastStarPos > -1:
        i = lastMatchPos + 1
        lastMatchPos += 1
        j = lastStarPos + 1
      ____:
        r.. False
    while j < lenP and p[j] __ "*":
      j += 1
    r.. j __ lenP
