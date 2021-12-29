from collections import Counter


class Solution(object):
  ___ findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sCount = Counter(s[:len(p) - 1])
    pCount = Counter(p)
    ans = []

    for i in range(len(p) - 1, len(s)):
      sCount[s[i]] += 1
      __ sCount == pCount:
        ans.append(i - len(p) + 1)
      sCount[s[i - len(p) + 1]] -= 1
      __ sCount[s[i - len(p) + 1]] == 0:
        del sCount[s[i - len(p) + 1]]
    return ans
