class TrieNode(object):
  ___ __init__(self):
    self.children = {}
    self.isWord = False
    self.word = ""


class Solution(object):
  ___ replaceWords(self, d.., sentence):
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
      p.isWord = True
      p.word = word

    words = sentence.s..
    ___ i __ r..(l..(words)):
      p = root
      ___ c __ words[i]:
        __ c __ p.children:
          p = p.children[c]
          __ p.isWord:
            words[i] = p.word
            break
        ____:
          break
    r.. " ".join(words)
