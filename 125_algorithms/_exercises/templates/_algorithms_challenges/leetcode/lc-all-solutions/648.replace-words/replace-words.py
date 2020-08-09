class TrieNode(object
  ___ __init__(self
    self.children = {}
    self.isWord = False
    self.word = ""


class Solution(object
  ___ replaceWords(self, dict, sentence
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """
    root = TrieNode()
    for word in dict:
      p = root
      for c in word:
        __ c not in p.children:
          p.children[c] = TrieNode()
        p = p.children[c]
      p.isWord = True
      p.word = word

    words = sentence.split()
    for i in range(le.(words)):
      p = root
      for c in words[i]:
        __ c in p.children:
          p = p.children[c]
          __ p.isWord:
            words[i] = p.word
            break
        ____
          break
    r_ " ".join(words)
