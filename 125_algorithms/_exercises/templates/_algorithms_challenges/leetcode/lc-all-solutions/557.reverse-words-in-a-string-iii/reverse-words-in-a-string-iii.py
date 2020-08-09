class Solution(object
  ___ reverseWords(self, s
    """
    :type s: str
    :rtype: str
    """
    s = s.split()
    for i, word in enumerate(s
      s[i] = word[::-1]
    r_ " ".join(s)
