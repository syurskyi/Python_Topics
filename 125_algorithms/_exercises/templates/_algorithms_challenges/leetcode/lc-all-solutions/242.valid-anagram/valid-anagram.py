class Solution(object
  ___ isAnagram(self, s, t
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    __ not le.(s) __ le.(t
      r_ False

    sHash = tHash = 1
    sCount = [0] * 26
    tCount = [0] * 26
    p1 = 2903
    p2 = 29947
    for i in range(0, le.(s)):
      sCount[ord(s[i]) - ord('a')] += 1
      tCount[ord(t[i]) - ord('a')] += 1

    for i in range(0, 26
      sHash = sHash * p1 + sCount[i]
      tHash = tHash * p1 + tCount[i]
      p1 *= p2
    r_ sHash __ tHash
