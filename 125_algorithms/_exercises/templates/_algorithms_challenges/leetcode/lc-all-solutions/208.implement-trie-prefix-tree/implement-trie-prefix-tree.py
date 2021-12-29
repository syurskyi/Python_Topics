class TrieNode(object):
  ___ __init__(self):
    """
    Initialize your data structure here.
    """
    self.children = [N..] * 26
    self.isWord = False
    self.word = ""


class Trie(object):

  ___ __init__(self):
    self.root = TrieNode()

  ___ insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    p = self.root
    ___ c __ word:
      cVal = ord(c) - ord("a")
      __ p.children[cVal]:
        p = p.children[cVal]
      ____:
        newNode = TrieNode()
        p.children[cVal] = newNode
        p = newNode

    p.isWord = True
    p.word = word

  ___ helper(self, word):
    p = self.root
    ___ c __ word:
      cVal = ord(c) - ord("a")
      __ p.children[cVal]:
        p = p.children[cVal]
      ____:
        r.. N..
    r.. p

  ___ search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    p = self.helper(word)
    __ p a.. p.isWord:
      r.. True
    r.. False

  ___ startsWith(self, prefix):
    """
    Returns if there is any word in the trie
    that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    __ self.helper(prefix):
      r.. True
    r.. False

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
