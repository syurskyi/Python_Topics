c_ Solution(o..):
  ___ _lengthOfLongestSubstring  s):
    """
    :type s: str
    :rtype: int
    """
    d = c...defaultdict(i..)
    l = ans = 0
    ___ i, c __ e..(s):
      w.... l > 0 a.. d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = m..(ans, l)
    r.. ans

  ___ lengthOfLongestSubstring  s):
    d    # dict
    start = 0
    ans = 0
    ___ i, c __ e..(s):
      __ c __ d:
        start = m..(start, d[c] + 1)
      d[c] = i
      ans = m..(ans, i - start + 1)
    r.. ans
