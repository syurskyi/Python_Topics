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


c_ TrieNode:
    ___ - ):
        """
        Initialize your data structure here.
        """
        # node value depends on the parent's hash mapping
        ended = F..
        children    # dict


c_ WordDictionary:
    ___ - ):
        """
        initialize your data structure here.
        """
        root = TrieNode()

    ___ addWord  word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = root
        ___ w __ word:
            __ w n.. __ cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = T..

    ___ s..  word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one
        letter.
        :type word: str
        :rtype: bool
        """
        r.. __search(word, root)

    ___ __search  word, cur):
        __ n.. word:
            r.. cur.ended

        w = word[0]
        __ w != ".":
            __ w __ cur.children:
                r.. __search(word[1:], cur.children[w])
            ____:
                r.. F..
        ____:
            ___ child __ cur.children.v..
                __ __search(word[1:], child):
                    r.. T..

        r.. F..

__ _______ __ _______
    dic = WordDictionary()
    dic.addWord("a")
    ... dic.s..(".") __ T..