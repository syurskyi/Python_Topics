class Solution(object):
  ___ strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    __ l..(haystack) __ l..(needle):
      __ haystack __ needle:
        r.. 0
      ____:
        r.. -1

    ___ i __ r..(0, l..(haystack)):
      k = i
      j = 0
      w.... j < l..(needle) a.. k < l..(haystack) a.. haystack[k] __ needle[j]:
        j += 1
        k += 1
      __ j __ l..(needle):
        r.. i
    r.. -1 __ needle ____ 0
