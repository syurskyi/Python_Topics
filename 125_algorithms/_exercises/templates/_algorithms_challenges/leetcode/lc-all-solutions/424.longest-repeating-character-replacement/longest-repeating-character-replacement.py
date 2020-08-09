from collections ______ deque


class Solution(object
  ___ characterReplacement(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ans = 0
    d = {}
    start = 0
    maxCount = 0
    window = deque([])
    ___ end in range(0, le.(s)):
      d[s[end]] = d.get(s[end], 0) + 1
      maxCount = max(maxCount, d[s[end]])
      __ end - start + 1 - maxCount > k:
        d[s[start]] -= 1
        start += 1
      ans = max(ans, end - start + 1)
    r_ ans
