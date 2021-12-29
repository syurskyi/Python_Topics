class Solution(object):
  ___ strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    __ len(haystack) == len(needle):
      __ haystack == needle:
        return 0
      else:
        return -1

    for i in range(0, len(haystack)):
      k = i
      j = 0
      while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
        j += 1
        k += 1
      __ j == len(needle):
        return i
    return -1 __ needle else 0
