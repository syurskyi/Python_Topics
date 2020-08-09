class Solution(object
  # brutal force TLE
  ___ _shortestPalindrome(self, s
    """
    :type s: str
    :rtype: str
    """

    ___ isPal(cand
      start, end = 0, le.(cand) - 1
      w___ start < end:
        __ cand[start] != cand[end]:
          r_ False
        start += 1
        end -= 1
      r_ True

    n = le.(s)
    ans = s[::-1] + s
    ansLen = 2 * le.(s)
    for i in reversed(range(0, le.(s) + 1)):
      newPal = s[i:][::-1] + s
      __ isPal(newPal) and n + le.(s) - i < ansLen:
        ansLen = n + le.(s) - i
        ans = newPal
    r_ ans

  ___ shortestPalindrome(self, s
    r = s[::-1]
    for i in range(le.(s) + 1
      __ s.startswith(r[i:]
        r_ r[:i] + s
