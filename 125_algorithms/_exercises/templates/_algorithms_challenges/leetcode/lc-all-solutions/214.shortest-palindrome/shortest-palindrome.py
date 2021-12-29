class Solution(object):
  # brutal force TLE
  ___ _shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    ___ isPal(cand):
      start, end = 0, len(cand) - 1
      while start < end:
        __ cand[start] != cand[end]:
          return False
        start += 1
        end -= 1
      return True

    n = len(s)
    ans = s[::-1] + s
    ansLen = 2 * len(s)
    for i in reversed(range(0, len(s) + 1)):
      newPal = s[i:][::-1] + s
      __ isPal(newPal) and n + len(s) - i < ansLen:
        ansLen = n + len(s) - i
        ans = newPal
    return ans

  ___ shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
      __ s.startswith(r[i:]):
        return r[:i] + s
