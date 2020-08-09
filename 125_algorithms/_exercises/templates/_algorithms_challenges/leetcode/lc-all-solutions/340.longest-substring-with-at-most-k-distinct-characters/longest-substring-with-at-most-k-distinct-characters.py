class Solution(object
  ___ lengthOfLongestSubstringKDistinct(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    j = 0
    ans = 0
    dict = {}
    for i in range(le.(s)):
      dict[s[i]] = dict.get(s[i], 0) + 1
      w___ j <= i and le.(dict) > k:
        dict[s[j]] -= 1
        __ dict[s[j]] __ 0:
          del dict[s[j]]
        j += 1
      ans = max(ans, i - j + 1)
    r_ ans
