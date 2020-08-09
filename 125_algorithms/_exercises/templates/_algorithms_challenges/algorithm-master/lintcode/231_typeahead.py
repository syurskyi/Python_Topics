class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ __init__(self, dict
        self.map = {}
        n = 0
        ___ key in dict:
            n = le.(key)
            ___ l in range(n
                ___ r in range(l + 1, n + 1
                    substr = key[l:r]
                    __ substr not in self.map:
                        self.map[substr] = [key]
                    ____ self.map[substr][-1] != key:
                        self.map[substr].append(key)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ search(self, str
        __ str in self.map:
            r_ self.map[str]
        r_ []


# Solution2
'''
This solution does not meet the demand.
Since the description said 'return all words that contains the string as a substring.'

But its a good solution for the auto-completion
'''
class Trie:
    ___ __init__(self
        self.root = self.new_node()

    ___ new_node(self
        r_ {
            'result': [],
            'children': {}
        }

    ___ put(self, key
        __ not key:
            r_
        ___ word in key.split(
            self._put(word, key)

    ___ _put(self, word, key
        parent = self.root
        ___ char in word.lower(
            __ char not in parent['children']:
                parent['children'][char] = self.new_node()
            parent = parent['children'][char]
            parent['result'].append(key)

    ___ search(self, key
        __ not key:
            r_ []
        parent = self.root
        ___ char in key.lower(
            __ char not in parent['children']:
                r_ []
            parent = parent['children'][char]
        r_ parent['result']

    # To support search with 2+ word
    # ___ search(self, key
    #     if not key:
    #         return []
    #     result = []
    #     for word in key.split(
    #         result += self._search(word)
    #     return result
    # ___ _search(self, word
    #     parent = self.root
    #     for char in word.lower(
    #         if char not in parent['children']:
    #             return []
    #         parent = parent['children'][char]
    #     return parent['result']

class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ __init__(self, dict
        self.trie = Trie()
        ___ word in dict:
            self.trie.put(word)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ search(self, str
        r_ self.trie.search(str)
