c_ Trie:
    ___ -
        root    # dict

    ___ insert  s__
        __ n.. s__:
            r..
        parent root
        ___ char __ s__:
            __ char __ parent:
                parent parent[char]
            ____
                parent[char]    # dict
                parent parent[char]
        parent '_end'  = T..

    ___ s..  s__
        __ n.. s__:
            r.. F..
        parent root
        ___ char __ s__:
            __ char __ parent:
                parent parent[char]
            ____
                r.. F..
        r.. T..

    ___ search_in_regex  s__
        __ n.. s__:
            r.. F..
        r.. _search_in_regex(s__, root, 0)

    ___ _search_in_regex  s__, parent, i
        __ i __ l..(s__
            r.. parent.g.. '_end', F..)
        result F..
        __ s__[i] __ '.':
            ___ child __ parent:
                __ child[0] !_ '_' a.. _search_in_regex(s__, parent[child], i + 1
                    result T..
        ____ s__[i] __ parent:
            __ _search_in_regex(s__, parent[s__[i]], i + 1
                result T..
        r.. result

c_ WordDictionary:
    ___ -
        trie Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    ___ addWord  word
        __ n.. word:
            r..
        trie.i.. word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    ___ s..  word
        __ n.. word:
            r.. F..
        r.. trie.search_in_regex(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
