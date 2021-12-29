class Solution(object):
  ___ longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    left = right = 0
    n = l..(s)
    ___ i __ r..(n - 1):
      __ 2 * (n - i) + 1 < right - left + 1:
        break
      l = r = i
      w.... l >= 0 a.. r < n a.. s[l] __ s[r]:
        l -= 1
        r += 1
      __ r - l - 2 > right - left:
        left = l + 1
        right = r - 1
      l = i
      r = i + 1
      w.... l >= 0 a.. r < n a.. s[l] __ s[r]:
        l -= 1
        r += 1
      __ r - l - 2 > right - left:
        left = l + 1
        right = r - 1
    r.. s[left:right + 1]
