class ValidWordAbbr(object):
  ___ __init__(self, dictionary):
    """
    initialize your data structure here.
    :type dictionary: List[str]
    """
    self.d = {}
    self.d.. = dictionary = set(dictionary)
    ___ word __ dictionary:
      wordLen = l..(word)
      __ wordLen > 2:
        key = word[0] + str(wordLen - 2) + word[-1]
        self.d[key] = self.d.get(key, 0) + 1
      ____:
        self.d[word] = self.d.get(word, 0) + 1

  ___ isUnique(self, word):
    """
    check if a word is unique.
    :type word: str
    :rtype: bool
    """
    wordLen = l..(word)
    key = N..
    __ wordLen > 2:
      key = word[0] + str(wordLen - 2) + word[-1]
    ____:
      key = word
    __ key __ self.d:
      __ self.d[key] __ 1 and word __ self.d..:
        r.. True
      r.. False
    ____:
      r.. True

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
