class ValidWordAbbr(object
  ___ __init__(self, dictionary
    """
    initialize your data structure here.
    :type dictionary: List[str]
    """
    self.d = {}
    self.dict = dictionary = set(dictionary)
    for word in dictionary:
      wordLen = le.(word)
      __ wordLen > 2:
        key = word[0] + str(wordLen - 2) + word[-1]
        self.d[key] = self.d.get(key, 0) + 1
      ____
        self.d[word] = self.d.get(word, 0) + 1

  ___ isUnique(self, word
    """
    check if a word is unique.
    :type word: str
    :rtype: bool
    """
    wordLen = le.(word)
    key = None
    __ wordLen > 2:
      key = word[0] + str(wordLen - 2) + word[-1]
    ____
      key = word
    __ key in self.d:
      __ self.d[key] __ 1 and word in self.dict:
        r_ True
      r_ False
    ____
      r_ True

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
