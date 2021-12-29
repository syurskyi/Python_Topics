class TrieNode:
  ___ __init__(self):
    self.neighbours = {}
    self.isWord = False


class Trie:
  ___ __init__(self):
    self.root = TrieNode()

  ___ addWord(self, word):
    root = self.root
    ___ i __ r..(0, l..(word)):
      c = word[i]
      __ c __ root.neighbours:
        root = root.neighbours[c]
      ____:
        newnode = TrieNode()
        root.neighbours[c] = newnode
        root = root.neighbours[c]
    root.isWord = True


class WordDictionary:
  ___ __init__(self):
    self.trie = Trie()
    self.cache = set([])

  ___ addWord(self, word):
    self.trie.addWord(word)
    self.cache.add(word)

  ___ search(self, word):
    __ word __ self.cache:
      r.. True

    ___ dfsHelper(root, word, index):
      __ n.. root:
        r.. False

      __ l..(word) __ index:
        __ root.isWord:
          r.. True
        r.. False

      __ word[index] != ".":
        __ dfsHelper(root.neighbours.get(word[index], N..), word, index + 1):
          r.. True
      ____:
        ___ nbr __ root.neighbours:
          __ dfsHelper(root.neighbours[nbr], word, index + 1):
            r.. True
      r.. False

    r.. dfsHelper(self.trie.root, word, 0)
