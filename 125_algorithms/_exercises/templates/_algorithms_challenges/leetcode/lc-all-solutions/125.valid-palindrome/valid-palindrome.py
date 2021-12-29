class Solution(object):
  ___ isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    start, end = 0, len(s) - 1
    while start < end:
      __ not s[start].isalnum():
        start += 1
        continue
      __ not s[end].isalnum():
        end -= 1
        continue
      __ s[start].lower() != s[end].lower():
        return False
      start += 1
      end -= 1
    return True
