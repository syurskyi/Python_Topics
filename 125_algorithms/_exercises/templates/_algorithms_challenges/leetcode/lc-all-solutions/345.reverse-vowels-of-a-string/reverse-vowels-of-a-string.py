______ string


class Solution(object
  ___ reverseVowels(self, s
    """
    :type s: str
    :rtype: str
    """
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    s = list(s)
    start, end = 0, le.(s) - 1
    w___ start < end:
      __ s[start] not in vowels:
        start += 1
      ____ s[end] not in vowels:
        end -= 1
      ____
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    r_ "".join(s)
