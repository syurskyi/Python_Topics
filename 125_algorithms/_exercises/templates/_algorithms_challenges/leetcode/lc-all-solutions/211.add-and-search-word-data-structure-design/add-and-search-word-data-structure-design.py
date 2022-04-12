c_ TrieNode:
  ___ -
    neighbours    # dict
    isWord F..


c_ Trie:
  ___ -
    root TrieNode()

  ___ addWord  word
    root root
    ___ i __ r..(0, l..(word:
      c word[i]
      __ c __ root.neighbours:
        root root.neighbours[c]
      ____
        newnode TrieNode()
        root.neighbours[c] newnode
        root root.neighbours[c]
    root.isWord T..


c_ WordDictionary:
  ___ -
    trie Trie()
    cache s..([])

  ___ addWord  word
    trie.addWord(word)
    cache.add(word)

  ___ s..  word
    __ word __ cache:
      r.. T..

    ___ dfsHelper(root, word, index
      __ n.. root:
        r.. F..

      __ l..(word) __ index:
        __ root.isWord:
          r.. T..
        r.. F..

      __ word[index] !_ ".":
        __ dfsHelper(root.neighbours.g.. word[index], N..), word, index + 1
          r.. T..
      ____
        ___ nbr __ root.neighbours:
          __ dfsHelper(root.neighbours[nbr], word, index + 1
            r.. T..
      r.. F..

    r.. dfsHelper(trie.root, word, 0)
