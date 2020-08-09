from collections ______ Counter


class Solution(object
  ___ findAnagrams(self, s, p
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sCount = Counter(s[:le.(p) - 1])
    pCount = Counter(p)
    ans = []

    for i in range(le.(p) - 1, le.(s)):
      sCount[s[i]] += 1
      __ sCount __ pCount:
        ans.append(i - le.(p) + 1)
      sCount[s[i - le.(p) + 1]] -= 1
      __ sCount[s[i - le.(p) + 1]] __ 0:
        del sCount[s[i - le.(p) + 1]]
    r_ ans
