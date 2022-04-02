"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
__author__ = 'Daniel'


c_ TrieNode:
    ___ -
        """
        Initialize your data structure here.
        """
        ended = F..
        children    # dict


c_ Trie:
    ___ -
        """
        Notice:
        * When insert new word, do not override the existing TrieNode
        * A flag to indicate whether there is a word ending here.
        """
        root = TrieNode()

    ___ insert  word
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = root
        ___ w __ word:
            __ w n.. __ cur.children:   # not override
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = T..

    ___ s..  word
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = root
        ___ w __ word:
            __ w __ cur.children:
                cur = cur.children[w]
            ____:
                r.. F..

        __ n.. cur.ended:  # not ended here
            r.. F..

        r.. T..

    ___ startsWith  prefix
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = root
        ___ w __ prefix:
            __ w __ cur.children:
                cur = cur.children[w]
            ____:
                r.. F..

        r.. T..