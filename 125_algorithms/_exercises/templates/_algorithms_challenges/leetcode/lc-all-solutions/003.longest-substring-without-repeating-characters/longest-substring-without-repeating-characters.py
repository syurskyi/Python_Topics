class Solution(object):
  ___ _lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = collections.defaultdict(int)
    l = ans = 0
    for i, c in enumerate(s):
      while l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = max(ans, l)
    return ans

  ___ lengthOfLongestSubstring(self, s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
      __ c in d:
        start = max(start, d[c] + 1)
      d[c] = i
      ans = max(ans, i - start + 1)
    return ans
