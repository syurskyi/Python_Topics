c_ ValidWordAbbr(o..):
  ___ - , dictionary):
    """
    initialize your data structure here.
    :type dictionary: List[str]
    """
    d    # dict
    d.. = dictionary = s..(dictionary)
    ___ word __ dictionary:
      wordLen = l..(word)
      __ wordLen > 2:
        key = word[0] + s..(wordLen - 2) + word[-1]
        d[key] = d.get(key, 0) + 1
      ____:
        d[word] = d.get(word, 0) + 1

  ___ isUnique  word):
    """
    check if a word is unique.
    :type word: str
    :rtype: bool
    """
    wordLen = l..(word)
    key = N..
    __ wordLen > 2:
      key = word[0] + s..(wordLen - 2) + word[-1]
    ____:
      key = word
    __ key __ d:
      __ d[key] __ 1 a.. word __ d..:
        r.. T..
      r.. F..
    ____:
      r.. T..

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
