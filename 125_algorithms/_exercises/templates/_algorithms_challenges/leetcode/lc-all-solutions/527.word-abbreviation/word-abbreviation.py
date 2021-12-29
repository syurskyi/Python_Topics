class Solution(object):
  ___ wordsAbbreviation(self, dict):
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
    for abbr, words in abbr2word.items():
      __ len(words) > 1:
        for word in words:
          for i in range(2, len(word)):
            prefix = word[:i]
            __ self.checkUnique(prefix, words):
              nabbr = self.getAbbr(word, prefix)
              word2abbr[word] = nabbr
              break
      else:
        word2abbr[words.pop()] = abbr
    return [word2abbr[word] for word in dict]

  ___ checkUnique(self, prefix, words):
    return sum(word.startswith(prefix) for word in words) == 1

  ___ getAbbr(self, word, prefix):
    abbr = prefix + str(len(word) - 1 - len(prefix)) + word[-1]
    return abbr __ len(abbr) < len(word) else word

  ___ getAbbreviation(self, word):
    abbr = word[0] + str(len(word) - 2) + word[-1]
    return abbr __ len(abbr) < len(word) else word
