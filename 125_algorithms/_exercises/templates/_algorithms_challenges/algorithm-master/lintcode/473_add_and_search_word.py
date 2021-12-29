class Trie:
    ___ __init__(self):
        self.root = {}

    ___ insert(self, string):
        __ not string:
            return
        parent = self.root
        for char in string:
            __ char in parent:
                parent = parent[char]
            else:
                parent[char] = {}
                parent = parent[char]
        parent['_end'] = True

    ___ search(self, string):
        __ not string:
            return False
        parent = self.root
        for char in string:
            __ char in parent:
                parent = parent[char]
            else:
                return False
        return True

    ___ search_in_regex(self, string):
        __ not string:
            return False
        return self._search_in_regex(string, self.root, 0)

    ___ _search_in_regex(self, string, parent, i):
        __ i == len(string):
            return parent.get('_end', False)
        result = False
        __ string[i] == '.':
            for child in parent:
                __ child[0] != '_' and self._search_in_regex(string, parent[child], i + 1):
                    result = True
        elif string[i] in parent:
            __ self._search_in_regex(string, parent[string[i]], i + 1):
                result = True
        return result

class WordDictionary:
    ___ __init__(self):
        self.trie = Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    ___ addWord(self, word):
        __ not word:
            return
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    ___ search(self, word):
        __ not word:
            return False
        return self.trie.search_in_regex(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
