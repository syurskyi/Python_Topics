class Solution(object
  ___ wordsAbbreviation(self, dict
    """
    :type dict: List[str]
    :rtype: List[str]
    """
    abbr2word = collections.defaultdict(set)
    word2abbr = {}

    # group words into abbreivations
    for word in dict:
      abbr = self.getAbbreviation(word)
      abbr2word[abbr].add(word)

    # resolve conflicts in each group
    for abbr, words in abbr2word.items(
      __ le.(words) > 1:
        for word in words:
          for i in range(2, le.(word)):
            prefix = word[:i]
            __ self.checkUnique(prefix, words
              nabbr = self.getAbbr(word, prefix)
              word2abbr[word] = nabbr
              break
      ____
        word2abbr[words.pop()] = abbr
    r_ [word2abbr[word] for word in dict]

  ___ checkUnique(self, prefix, words
    r_ sum(word.startswith(prefix) for word in words) __ 1

  ___ getAbbr(self, word, prefix
    abbr = prefix + str(le.(word) - 1 - le.(prefix)) + word[-1]
    r_ abbr __ le.(abbr) < le.(word) else word

  ___ getAbbreviation(self, word
    abbr = word[0] + str(le.(word) - 2) + word[-1]
    r_ abbr __ le.(abbr) < le.(word) else word
