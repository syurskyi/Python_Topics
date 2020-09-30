class Solution(object
  ___ _lengthOfLongestSubstring(self, s
    """
    :type s: str
    :rtype: int
    """
    d = collections.defaultdict(int)
    l = ans = 0
    ___ i, c __ enumerate(s
      w___ l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = ma.(ans, l)
    r_ ans

  ___ lengthOfLongestSubstring(self, s
    d = {}
    start = 0
    ans = 0
    ___ i, c __ enumerate(s
      __ c __ d:
        start = ma.(start, d[c] + 1)
      d[c] = i
      ans = ma.(ans, i - start + 1)
    r_ ans
