class Trie:
    ___ __init__(self
        self.root = {}

    ___ insert(self, string
        __ not string:
            r_
        parent = self.root
        ___ char in string:
            __ char in parent:
                parent = parent[char]
            ____
                parent[char] = {}
                parent = parent[char]
        parent['_end'] = True

    ___ search(self, string
        __ not string:
            r_ False
        parent = self.root
        ___ char in string:
            __ char in parent:
                parent = parent[char]
            ____
                r_ False
        r_ True

    ___ search_in_regex(self, string
        __ not string:
            r_ False
        r_ self._search_in_regex(string, self.root, 0)

    ___ _search_in_regex(self, string, parent, i
        __ i __ le.(string
            r_ parent.get('_end', False)
        result = False
        __ string[i] __ '.':
            ___ child in parent:
                __ child[0] != '_' and self._search_in_regex(string, parent[child], i + 1
                    result = True
        ____ string[i] in parent:
            __ self._search_in_regex(string, parent[string[i]], i + 1
                result = True
        r_ result

class WordDictionary:
    ___ __init__(self
        self.trie = Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    ___ addWord(self, word
        __ not word:
            r_
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    ___ search(self, word
        __ not word:
            r_ False
        r_ self.trie.search_in_regex(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
