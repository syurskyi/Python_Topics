c_ TrieNode(object):
  ___ - ):
    """
    Initialize your data structure here.
    """
    children = [N..] * 26
    isWord = F..
    word = ""


c_ Trie(object):

  ___ - ):
    root = TrieNode()

  ___ insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    p = root
    ___ c __ word:
      cVal = ord(c) - ord("a")
      __ p.children[cVal]:
        p = p.children[cVal]
      ____:
        newNode = TrieNode()
        p.children[cVal] = newNode
        p = newNode

    p.isWord = T..
    p.word = word

  ___ helper(self, word):
    p = root
    ___ c __ word:
      cVal = ord(c) - ord("a")
      __ p.children[cVal]:
        p = p.children[cVal]
      ____:
        r.. N..
    r.. p

  ___ s..(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    p = helper(word)
    __ p a.. p.isWord:
      r.. T..
    r.. F..

  ___ startsWith(self, prefix):
    """
    Returns if there is any word in the trie
    that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    __ helper(prefix):
      r.. T..
    r.. F..

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
