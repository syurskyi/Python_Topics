class Solution(object):
  ___ countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = l..(s)
    ans = 0
    ___ i __ r..(n):
      left = right = i
      while left >= 0 and right < n and s[left] __ s[right]:
        ans += 1
        left -= 1
        right += 1

      left = i
      right = i + 1
      while left >= 0 and right < n and s[left] __ s[right]:
        ans += 1
        left -= 1
        right += 1
    r.. ans
