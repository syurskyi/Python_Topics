class Solution(object
  ___ countSubstrings(self, s
    """
    :type s: str
    :rtype: int
    """
    n = le.(s)
    ans = 0
    for i in range(n
      left = right = i
      w___ left >= 0 and right < n and s[left] __ s[right]:
        ans += 1
        left -= 1
        right += 1

      left = i
      right = i + 1
      w___ left >= 0 and right < n and s[left] __ s[right]:
        ans += 1
        left -= 1
        right += 1
    r_ ans
