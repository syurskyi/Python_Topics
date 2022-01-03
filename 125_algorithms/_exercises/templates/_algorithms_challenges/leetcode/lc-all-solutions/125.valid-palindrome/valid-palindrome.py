c_ Solution(object):
  ___ isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    start, end = 0, l..(s) - 1
    w.... start < end:
      __ n.. s[start].i..
        start += 1
        continue
      __ n.. s[end].i..
        end -= 1
        continue
      __ s[start].l.. != s[end].l..:
        r.. F..
      start += 1
      end -= 1
    r.. T..
