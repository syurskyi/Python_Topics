class Trie:
    ___ __init__(self):
        self.root = {}

    ___ insert(self, string):
        __ n.. string:
            r..
        parent = self.root
        ___ char __ string:
            __ char __ parent:
                parent = parent[char]
            ____:
                parent[char] = {}
                parent = parent[char]
        parent['_end'] = True

    ___ search(self, string):
        __ n.. string:
            r.. False
        parent = self.root
        ___ char __ string:
            __ char __ parent:
                parent = parent[char]
            ____:
                r.. False
        r.. True

    ___ search_in_regex(self, string):
        __ n.. string:
            r.. False
        r.. self._search_in_regex(string, self.root, 0)

    ___ _search_in_regex(self, string, parent, i):
        __ i __ l..(string):
            r.. parent.get('_end', False)
        result = False
        __ string[i] __ '.':
            ___ child __ parent:
                __ child[0] != '_' and self._search_in_regex(string, parent[child], i + 1):
                    result = True
        ____ string[i] __ parent:
            __ self._search_in_regex(string, parent[string[i]], i + 1):
                result = True
        r.. result

class WordDictionary:
    ___ __init__(self):
        self.trie = Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    ___ addWord(self, word):
        __ n.. word:
            r..
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    ___ search(self, word):
        __ n.. word:
            r.. False
        r.. self.trie.search_in_regex(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
