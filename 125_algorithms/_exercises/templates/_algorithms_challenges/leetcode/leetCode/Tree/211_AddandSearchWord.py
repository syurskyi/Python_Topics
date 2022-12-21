#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
import collections


c.. WordDictionary o..
    # One faster, easy understand way
    # Refer to:
    # https://leetcode.com/discuss/69963/python-168ms-beat-100%25-solution
    ___ __init__(self
        self.words_dict = collections.defaultdict(list)

    ___ addWord  word
        __ word:
            self.words_dict[l..(word)].append(word)

    ___ search  word
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        """
        __ n.. word:
            r_ False
        ___ w __ self.words_dict[l..(word)]:
            is_match = True
            ___ i, ch __ enumerate(word
                __ ch != "." a.. ch != w[i]:
                    is_match = False
                    ______
            __ is_match:
                r_ True
        r_ False


c.. TrieNode(
    # Refer to: 208. Implement Trie
    ___ __init__(self
        self.is_word = False
        self.childrens _ # dict


c.. WordDictionary_Trie o..
    ___ __init__(self
        self.root = TrieNode()

    ___ addWord  word
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        ___ ch __ word:
            __ ch n.. __ cur_node.childrens:
                cur_node.childrens[ch] = TrieNode()
            cur_node = cur_node.childrens[ch]
        cur_node.is_word = True

    ___ search  word
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        """
        r_ self._dfs_searh(word, self.root)

    # Depth First Search the trie tree.
    ___ _dfs_searh  word, cur_node
        __ n.. word a.. cur_node.is_word:
            r_ True
        word_len = l..(word)
        ___ i __ r..(word_len
            ch = word[i]
            __ ch __ ".":
                ___ child_ch __ cur_node.childrens:
                    __ self._dfs_searh(word[i+1:],
                                       cur_node.childrens[child_ch]
                        r_ True
                r_ False
            ____
                __ ch n.. __ cur_node.childrens:
                    r_ False
                ____
                    cur_node = cur_node.childrens[ch]
        __ cur_node.is_word:
            r_ True
        ____
            r_ False

"""
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print wordDictionary.search("xad")
    print wordDictionary.search(".a")
    print wordDictionary.search(".ad")
    print wordDictionary.search("b.")
    print wordDictionary.search(".")
"""
