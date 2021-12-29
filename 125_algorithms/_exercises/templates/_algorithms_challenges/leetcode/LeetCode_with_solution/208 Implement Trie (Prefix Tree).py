"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
__author__ = 'Daniel'


class TrieNode:
    ___ __init__(self):
        """
        Initialize your data structure here.
        """
        self.ended = False
        self.children = {}


class Trie:
    ___ __init__(self):
        """
        Notice:
        * When insert new word, do not override the existing TrieNode
        * A flag to indicate whether there is a word ending here.
        """
        self.root = TrieNode()

    ___ insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            __ w not in cur.children:   # not override
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    ___ search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            __ w in cur.children:
                cur = cur.children[w]
            else:
                return False

        __ not cur.ended:  # not ended here
            return False

        return True

    ___ startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            __ w in cur.children:
                cur = cur.children[w]
            else:
                return False

        return True