c_ Solution(object):
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
    w.... i < l..(s):
      __ j < lenP a.. p[j] __ (s[i], "?"):
        i += 1
        j += 1
      ____ j < lenP a.. p[j] __ "*":
        lastMatchPos = i
        lastStarPos = j
        j += 1
      ____ lastStarPos > -1:
        i = lastMatchPos + 1
        lastMatchPos += 1
        j = lastStarPos + 1
      ____:
        r.. F..
    w.... j < lenP a.. p[j] __ "*":
      j += 1
    r.. j __ lenP
