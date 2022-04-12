c_ Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ - , d..
        map    # dict
        n 0
        ___ key __ d..:
            n l..(key)
            ___ l __ r..(n
                ___ r __ r..(l + 1, n + 1
                    substr key[l:r]
                    __ substr n.. __ map:
                        map[substr] [key]
                    ____ map[substr][-1] !_ key:
                        map[substr].a..(key)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ s..  s..
        __ s.. __ map:
            r.. map[s..]
        r.. []


# Solution2
'''
This solution does not meet the demand.
Since the description said 'return all words that contains the string as a substring.'

But its a good solution for the auto-completion
'''
c_ Trie:
    ___ -
        root new_node()

    ___ new_node
        r.. {
            'result': [],
            'children': {}
        }

    ___ put  key
        __ n.. key:
            r..
        ___ word __ key.s.. :
            _put(word, key)

    ___ _put  word, key
        parent root
        ___ char __ word.l..:
            __ char n.. __ parent 'children' :
                parent 'children' [char] new_node()
            parent parent 'children' [char]
            parent 'result' .a..(key)

    ___ s..  key
        __ n.. key:
            r.. []
        parent root
        ___ char __ key.l..:
            __ char n.. __ parent 'children' :
                r.. []
            parent parent 'children' [char]
        r.. parent 'result'

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

c_ Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    ___ - , d..
        trie Trie()
        ___ word __ d..:
            trie.put(word)

    """
    @param: str: a string
    @return: a list of words
    """
    ___ s..  s..
        r.. trie.s..(s..)
