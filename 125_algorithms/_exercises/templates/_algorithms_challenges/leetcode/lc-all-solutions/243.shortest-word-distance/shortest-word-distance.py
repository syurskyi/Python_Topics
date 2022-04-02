c_ Solution(o..
  ___ shortestDistance  words, word1, word2
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    idx1 = idx2 = -1
    ans = l..(words)
    ___ i __ r..(0, l..(words)):
      word = words[i]
      __ word __ (word1, word2
        __ word __ word1:
          idx1 = i
        ____ word __ word2:
          idx2 = i
        __ idx1 != -1 a.. idx2 != -1:
          ans = m..(ans, abs(idx2 - idx1))
    r.. ans
