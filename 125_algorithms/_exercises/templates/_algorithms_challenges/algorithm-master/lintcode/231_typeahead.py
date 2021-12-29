class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ __init__(self, d..):
        self.map = {}
        n = 0
        ___ key __ d..:
            n = l..(key)
            ___ l __ r..(n):
                ___ r __ r..(l + 1, n + 1):
                    substr = key[l:r]
                    __ substr n.. __ self.map:
                        self.map[substr] = [key]
                    ____ self.map[substr][-1] != key:
                        self.map[substr].a..(key)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ search(self, s..):
        __ s.. __ self.map:
            r.. self.map[s..]
        r.. []


# Solution2
'''
This solution does not meet the demand.
Since the description said 'return all words that contains the string as a substring.'

But its a good solution for the auto-completion
'''
class Trie:
    ___ __init__(self):
        self.root = self.new_node()

    ___ new_node(self):
        r.. {
            'result': [],
            'children': {}
        }

    ___ put(self, key):
        __ n.. key:
            r..
        ___ word __ key.s.. :
            self._put(word, key)

    ___ _put(self, word, key):
        parent = self.root
        ___ char __ word.lower():
            __ char n.. __ parent['children']:
                parent['children'][char] = self.new_node()
            parent = parent['children'][char]
            parent['result'].a..(key)

    ___ search(self, key):
        __ n.. key:
            r.. []
        parent = self.root
        ___ char __ key.lower():
            __ char n.. __ parent['children']:
                r.. []
            parent = parent['children'][char]
        r.. parent['result']

    # To support search with 2+ word
    # def search(self, key):
    #     if not key:
    #         return []
    #     result = []
    #     for word in key.split():
    #         result += self._search(word)
    #     return result
    # def _search(self, word):
    #     parent = self.root
    #     for char in word.lower():
    #         if char not in parent['children']:
    #             return []
    #         parent = parent['children'][char]
    #     return parent['result']

class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ __init__(self, d..):
        self.trie = Trie()
        ___ word __ d..:
            self.trie.put(word)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ search(self, s..):
        r.. self.trie.search(s..)
