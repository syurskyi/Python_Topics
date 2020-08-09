class Solution(object
  ___ findRepeatedDnaSequences(self, s
    """
    :type s: str
    :rtype: List[str]
    """
    d = {}
    ans = []
    for i in range(le.(s) - 9
      key = s[i:i + 10]
      __ key in d:
        d[key] += 1
        __ d[key] __ 2:
          ans.append(key)
      ____
        d[key] = 1
    r_ ans
