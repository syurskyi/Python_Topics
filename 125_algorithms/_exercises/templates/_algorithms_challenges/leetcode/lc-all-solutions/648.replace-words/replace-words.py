c_ TrieNode(o..
  ___ -
    children    # dict
    isWord = F..
    word = ""


c_ Solution(o..
  ___ replaceWords  d.., sentence
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """
    root = TrieNode()
    ___ word __ d..:
      p = root
      ___ c __ word:
        __ c n.. __ p.children:
          p.children[c] = TrieNode()
        p = p.children[c]
      p.isWord = T..
      p.word = word

    words = sentence.s..
    ___ i __ r..(l..(words:
      p = root
      ___ c __ words[i]:
        __ c __ p.children:
          p = p.children[c]
          __ p.isWord:
            words[i] = p.word
            _____
        ____:
          _____
    r.. " ".j..(words)
