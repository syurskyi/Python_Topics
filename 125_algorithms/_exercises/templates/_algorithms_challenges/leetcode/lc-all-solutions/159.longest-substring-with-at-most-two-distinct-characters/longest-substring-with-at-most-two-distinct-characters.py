c_ Solution(o..
  ___ lengthOfLongestSubstringTwoDistinct  s
    """
    :type s: str
    :rtype: int
    """
    r.. lengthOfLongestSubstringKDistinct(s, 2)

  ___ lengthOfLongestSubstringKDistinct  s, k
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    __ k __ 0:
      r.. 0
    ans = 0
    j = 0
    score = 0
    chashmap    # dict
    ___ i __ r..(0, l..(s:
      w.... j < l..(s) a.. (score < k o. chashmap.g.. s[j], 0) != 0
        __ chashmap.g.. s[j], 0) __ 0:
          score += 1
        chashmap[s[j]] = chashmap.g.. s[j], 0) + 1
        j += 1

      ans = m..(ans, j - i)
      chashmap[s[i]] -= 1
      __ chashmap[s[i]] __ 0:
        score -= 1
    r.. ans
