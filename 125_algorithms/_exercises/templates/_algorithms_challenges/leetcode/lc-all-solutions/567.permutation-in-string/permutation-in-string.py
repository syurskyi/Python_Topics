class Solution(object
  ___ checkInclusion(self, s1, s2
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    d = {}
    n = le.(s1)
    for c in s1:
      d[c] = d.get(c, 0) + 1
    window = {}
    for i, c in enumerate(s2
      window[c] = window.get(c, 0) + 1
      __ i >= le.(s1
        window[s2[i - n]] = window.get(s2[i - n], 0) - 1
        __ window[s2[i - n]] __ 0:
          del window[s2[i - n]]
      __ window __ d:
        r_ True
    r_ False
