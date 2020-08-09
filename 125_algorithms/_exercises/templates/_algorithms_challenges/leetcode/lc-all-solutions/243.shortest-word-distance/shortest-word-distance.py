class Solution(object
  ___ shortestDistance(self, words, word1, word2
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    idx1 = idx2 = -1
    ans = le.(words)
    for i in range(0, le.(words)):
      word = words[i]
      __ word in (word1, word2
        __ word __ word1:
          idx1 = i
        ____ word __ word2:
          idx2 = i
        __ idx1 != -1 and idx2 != -1:
          ans = min(ans, abs(idx2 - idx1))
    r_ ans
