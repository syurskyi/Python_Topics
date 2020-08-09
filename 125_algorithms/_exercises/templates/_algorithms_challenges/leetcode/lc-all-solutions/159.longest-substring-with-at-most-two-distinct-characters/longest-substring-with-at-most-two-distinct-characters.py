class Solution(object
  ___ lengthOfLongestSubstringTwoDistinct(self, s
    """
    :type s: str
    :rtype: int
    """
    r_ self.lengthOfLongestSubstringKDistinct(s, 2)

  ___ lengthOfLongestSubstringKDistinct(self, s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    __ k __ 0:
      r_ 0
    ans = 0
    j = 0
    score = 0
    chashmap = {}
    for i in range(0, le.(s)):
      w___ j < le.(s) and (score < k or chashmap.get(s[j], 0) != 0
        __ chashmap.get(s[j], 0) __ 0:
          score += 1
        chashmap[s[j]] = chashmap.get(s[j], 0) + 1
        j += 1

      ans = max(ans, j - i)
      chashmap[s[i]] -= 1
      __ chashmap[s[i]] __ 0:
        score -= 1
    r_ ans
