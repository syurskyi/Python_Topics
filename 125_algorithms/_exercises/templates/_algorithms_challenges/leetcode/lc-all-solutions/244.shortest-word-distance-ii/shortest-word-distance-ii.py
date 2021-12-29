class WordDistance(object):
  ___ __init__(self, words):
    """
    initialize your data structure here.
    :type words: List[str]
    """
    self.d = {}
    ___ i __ r..(0, l..(words)):
      self.d[words[i]] = self.d.get(words[i], []) + [i]

  ___ shortest(self, word1, word2):
    """
    Adds a word into the data structure.
    :type word1: str
    :type word2: str
    :rtype: int
    """
    l1 = self.d[word1]
    l2 = self.d[word2]
    i = j = 0
    ans = float("inf")
    while i < l..(l1) and j < l..(l2):
      ans = m..(ans, abs(l1[i] - l2[j]))
      __ l1[i] > l2[j]:
        j += 1
      ____:
        i += 1
    r.. ans

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
