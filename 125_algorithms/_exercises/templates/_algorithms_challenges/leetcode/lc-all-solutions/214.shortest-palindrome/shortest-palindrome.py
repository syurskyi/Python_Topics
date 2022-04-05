c_ Solution(o..
  # brutal force TLE
  ___ _shortestPalindrome  s
    """
    :type s: str
    :rtype: str
    """

    ___ isPal(cand
      start, end = 0, l..(cand) - 1
      w.... start < end:
        __ cand[start] != cand[end]:
          r.. F..
        start += 1
        end -= 1
      r.. T..

    n = l..(s)
    ans = s[::-1] + s
    ansLen = 2 * l..(s)
    ___ i __ r..(r..(0, l..(s) + 1:
      newPal = s[i:][::-1] + s
      __ isPal(newPal) a.. n + l..(s) - i < ansLen:
        ansLen = n + l..(s) - i
        ans = newPal
    r.. ans

  ___ shortestPalindrome  s
    r = s[::-1]
    ___ i __ r..(l..(s) + 1
      __ s.s.. r[i:]
        r.. r[:i] + s
