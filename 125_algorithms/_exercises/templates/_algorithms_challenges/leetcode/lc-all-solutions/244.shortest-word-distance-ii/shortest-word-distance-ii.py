c_ WordDistance(o..
  ___ - , words
    """
    initialize your data structure here.
    :type words: List[str]
    """
    d    # dict
    ___ i __ r..(0, l..(words:
      d[words[i]] d.g.. words[i], []) + [i]

  ___ shortest  word1, word2
    """
    Adds a word into the data structure.
    :type word1: str
    :type word2: str
    :rtype: int
    """
    l1 d[word1]
    l2 d[word2]
    i j 0
    ans f__("inf")
    w.... i < l..(l1) a.. j < l..(l2
      ans m..(ans, a..(l1[i] - l2[j]
      __ l1[i] > l2[j]:
        j += 1
      ____
        i += 1
    r.. ans

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
