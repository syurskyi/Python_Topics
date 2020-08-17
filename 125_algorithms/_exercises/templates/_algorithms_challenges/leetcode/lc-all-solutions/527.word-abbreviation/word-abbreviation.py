class Solution(object
  ___ wordsAbbreviation(self, dict
    """
    :type dict: List[str]
    :rtype: List[str]
    """
    abbr2word = collections.defaultdict(set)
    word2abbr = {}

    # group words into abbreivations
    ___ word in dict:
      abbr = self.getAbbreviation(word)
      abbr2word[abbr].add(word)

    # resolve conflicts in each group
    ___ abbr, words in abbr2word.items(
      __ le.(words) > 1:
        ___ word in words:
          ___ i in range(2, le.(word)):
            prefix = word[:i]
            __ self.checkUnique(prefix, words
              nabbr = self.getAbbr(word, prefix)
              word2abbr[word] = nabbr
              break
      ____
        word2abbr[words.p..] = abbr
    r_ [word2abbr[word] ___ word in dict]

  ___ checkUnique(self, prefix, words
    r_ su.(word.startswith(prefix) ___ word in words) __ 1

  ___ getAbbr(self, word, prefix
    abbr = prefix + str(le.(word) - 1 - le.(prefix)) + word[-1]
    r_ abbr __ le.(abbr) < le.(word) else word

  ___ getAbbreviation(self, word
    abbr = word[0] + str(le.(word) - 2) + word[-1]
    r_ abbr __ le.(abbr) < le.(word) else word
