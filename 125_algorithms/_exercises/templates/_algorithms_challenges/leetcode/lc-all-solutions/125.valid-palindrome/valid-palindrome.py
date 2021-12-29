class Solution(object):
  ___ isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    start, end = 0, l..(s) - 1
    w.... start < end:
      __ n.. s[start].isalnum():
        start += 1
        continue
      __ n.. s[end].isalnum():
        end -= 1
        continue
      __ s[start].lower() != s[end].lower():
        r.. False
      start += 1
      end -= 1
    r.. True
