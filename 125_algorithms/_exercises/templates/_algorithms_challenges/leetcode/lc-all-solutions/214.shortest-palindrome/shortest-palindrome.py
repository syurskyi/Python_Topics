class Solution(object):
  # brutal force TLE
  ___ _shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    ___ isPal(cand):
      start, end = 0, l..(cand) - 1
      while start < end:
        __ cand[start] != cand[end]:
          r.. False
        start += 1
        end -= 1
      r.. True

    n = l..(s)
    ans = s[::-1] + s
    ansLen = 2 * l..(s)
    ___ i __ reversed(r..(0, l..(s) + 1)):
      newPal = s[i:][::-1] + s
      __ isPal(newPal) and n + l..(s) - i < ansLen:
        ansLen = n + l..(s) - i
        ans = newPal
    r.. ans

  ___ shortestPalindrome(self, s):
    r = s[::-1]
    ___ i __ r..(l..(s) + 1):
      __ s.startswith(r[i:]):
        r.. r[:i] + s
