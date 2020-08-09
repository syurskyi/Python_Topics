"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can
represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
__author__ = 'Daniel'


class TrieNode:
    ___ __init__(self
        """
        Initialize your data structure here.
        """
        # node value depends on the parent's hash mapping
        self.ended = False
        self.children = {}


class WordDictionary:
    ___ __init__(self
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    ___ addWord(self, word
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            __ w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    ___ search(self, word
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one
        letter.
        :type word: str
        :rtype: bool
        """
        r_ self.__search(word, self.root)

    ___ __search(self, word, cur
        __ not word:
            r_ cur.ended

        w = word[0]
        __ w != ".":
            __ w in cur.children:
                r_ self.__search(word[1:], cur.children[w])
            ____
                r_ False
        ____
            for child in cur.children.values(
                __ self.__search(word[1:], child
                    r_ True

        r_ False

__ __name__ __ "__main__":
    dic = WordDictionary()
    dic.addWord("a")
    assert dic.search(".") __ True