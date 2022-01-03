c_ Trie:
    ___ - ):
        root    # dict

    ___ insert(self, string):
        __ n.. string:
            r..
        parent = root
        ___ char __ string:
            __ char __ parent:
                parent = parent[char]
            ____:
                parent[char]    # dict
                parent = parent[char]
        parent['_end'] = T..

    ___ s..(self, string):
        __ n.. string:
            r.. F..
        parent = root
        ___ char __ string:
            __ char __ parent:
                parent = parent[char]
            ____:
                r.. F..
        r.. T..

    ___ search_in_regex(self, string):
        __ n.. string:
            r.. F..
        r.. _search_in_regex(string, root, 0)

    ___ _search_in_regex(self, string, parent, i):
        __ i __ l..(string):
            r.. parent.get('_end', F..)
        result = F..
        __ string[i] __ '.':
            ___ child __ parent:
                __ child[0] != '_' a.. _search_in_regex(string, parent[child], i + 1):
                    result = T..
        ____ string[i] __ parent:
            __ _search_in_regex(string, parent[string[i]], i + 1):
                result = T..
        r.. result

c_ WordDictionary:
    ___ - ):
        trie = Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    ___ addWord(self, word):
        __ n.. word:
            r..
        trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    ___ s..(self, word):
        __ n.. word:
            r.. F..
        r.. trie.search_in_regex(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
