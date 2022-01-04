c_ Solution(object):
  ___ wordsAbbreviation(self, d..):
    """
    :type dict: List[str]
    :rtype: List[str]
    """
    abbr2word = c...defaultdict(set)
    word2abbr    # dict

    # group words into abbreivations
    ___ word __ d..:
      abbr = getAbbreviation(word)
      abbr2word[abbr].add(word)

    # resolve conflicts in each group
    ___ abbr, words __ abbr2word.i..:
      __ l..(words) > 1:
        ___ word __ words:
          ___ i __ r..(2, l..(word)):
            prefix = word[:i]
            __ checkUnique(prefix, words):
              nabbr = getAbbr(word, prefix)
              word2abbr[word] = nabbr
              break
      ____:
        word2abbr[words.pop()] = abbr
    r.. [word2abbr[word] ___ word __ d..]

  ___ checkUnique(self, prefix, words):
    r.. s..(word.startswith(prefix) ___ word __ words) __ 1

  ___ getAbbr(self, word, prefix):
    abbr = prefix + s..(l..(word) - 1 - l..(prefix)) + word[-1]
    r.. abbr __ l..(abbr) < l..(word) ____ word

  ___ getAbbreviation(self, word):
    abbr = word[0] + s..(l..(word) - 2) + word[-1]
    r.. abbr __ l..(abbr) < l..(word) ____ word
