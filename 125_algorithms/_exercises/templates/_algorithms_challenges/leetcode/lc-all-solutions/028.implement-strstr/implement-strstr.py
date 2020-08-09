class Solution(object
  ___ strStr(self, haystack, needle
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    __ le.(haystack) __ le.(needle
      __ haystack __ needle:
        r_ 0
      ____
        r_ -1

    for i in range(0, le.(haystack)):
      k = i
      j = 0
      w___ j < le.(needle) and k < le.(haystack) and haystack[k] __ needle[j]:
        j += 1
        k += 1
      __ j __ le.(needle
        r_ i
    r_ -1 __ needle else 0
