class TrieNode:
  ___ __init__(self):
    self.neighbours = {}
    self.isWord = False


class Trie:
  ___ __init__(self):
    self.root = TrieNode()

  ___ addWord(self, word):
    root = self.root
    for i in range(0, len(word)):
      c = word[i]
      __ c in root.neighbours:
        root = root.neighbours[c]
      else:
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
    __ word in self.cache:
      return True

    ___ dfsHelper(root, word, index):
      __ not root:
        return False

      __ len(word) == index:
        __ root.isWord:
          return True
        return False

      __ word[index] != ".":
        __ dfsHelper(root.neighbours.get(word[index], None), word, index + 1):
          return True
      else:
        for nbr in root.neighbours:
          __ dfsHelper(root.neighbours[nbr], word, index + 1):
            return True
      return False

    return dfsHelper(self.trie.root, word, 0)
