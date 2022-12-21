#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/49529/my-python-solution


c.. TrieNode o..
    ___ __init__(self
        self.children _ # dict
        self.is_word = False


c.. Trie o..
    ___ __init__(self
        self.root = TrieNode()

    ___ insert  word
        # Inserts a word into the trie.
        cur_node = self.root
        ___ ch __ word:
            __ ch n.. __ cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
        cur_node.is_word = True

    ___ search  word
        # Returns if the word is in the trie.
        cur_node = self.root
        ___ ch __ word:
            __ ch n.. __ cur_node.children:
                r_ False
            cur_node = cur_node.children[ch]
        r_ cur_node.is_word

    ___ startsWith  prefix
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        cur_node = self.root
        ___ ch __ prefix:
            __ ch n.. __ cur_node.children:
                r_ False
            cur_node = cur_node.children[ch]
        r_ True

"""
if __name__ == '__main__':
    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")
    trie.insert("rental")
    print trie.search("apps")
    print trie.search("app")
    print trie.search("ad")
"""
