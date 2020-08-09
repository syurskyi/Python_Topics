class Solution(object
  ___ isMatch(self, s, p
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    i = j = 0
    lenS = le.(s)
    lenP = le.(p)
    lastMatchPos = 0
    lastStarPos = -1
    w___ i < le.(s
      __ j < lenP and p[j] in (s[i], "?"
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
      ____
        r_ False
    w___ j < lenP and p[j] __ "*":
      j += 1
    r_ j __ lenP
