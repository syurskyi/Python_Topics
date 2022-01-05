_______ s__


c_ Solution(o..):
  ___ reverseVowels  s):
    """
    :type s: str
    :rtype: str
    """
    vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
    s = l..(s)
    start, end = 0, l..(s) - 1
    w.... start < end:
      __ s[start] n.. __ vowels:
        start += 1
      ____ s[end] n.. __ vowels:
        end -= 1
      ____:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    r.. "".j..(s)
