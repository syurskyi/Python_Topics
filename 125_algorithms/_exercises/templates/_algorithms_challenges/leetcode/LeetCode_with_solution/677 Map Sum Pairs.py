#!/usr/bin/python3
"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string
represents the key and the integer represents the value. If the key already
existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you
need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum:

    ___ __init__(self):
        """
        Initialize your data structure here.

        Trie

        update using delta
        """
        ____ collections _______ defaultdict

        class TrieNode:
            ___ __init__(self, chr, s.., val):
                self.chr = chr
                self.s.. = s..
                self.val = val
                self.children = defaultdict(l....: N..)

        class Trie:
            ___ __init__(self):
                self.root = TrieNode(N.., 0, 0)  # dummy root

            ___ insert(self, cur, key, i, val):
                __ n.. cur:
                    cur = TrieNode(key[i], 0, 0)

                __ i __ l..(key) - 1:
                    delta = val - cur.val
                    cur.val = val
                ____:
                    cur.children[key[i+1]], delta = self.insert(cur.children[key[i+1]], key, i + 1, val)

                cur.s.. += delta
                r.. cur, delta

        self.trie = Trie()

    ___ insert(self, key: s.., val: int) -> N..
        root = self.trie.root
        root.children[key[0]], _ = self.trie.insert(root.children[key[0]], key, 0, val)

    ___ s..(self, prefix: s..) -> int:
        node = self.trie.root
        ___ a __ prefix:
            __ a n.. __ node.children:
                r.. 0

            node = node.children[a]

        r.. node.s..


class MapSum2:

    ___ __init__(self):
        """
        Initialize your data structure here.

        Trie

        update using delta
        """
        class TrieNode:
            ___ __init__(self, chr, s.., val):
                self.chr = chr
                self.s.. = s..
                self.val = val
                self.children = {}

        class Trie:
            ___ __init__(self):
                self.root = TrieNode(N.., 0, 0)  # dummy root

            ___ insert(self, pi, key, i, val):
                __ key[i] n.. __ pi.children:
                    cur = TrieNode(key[i], 0, 0)
                    pi.children[key[i]] = cur

                cur = pi.children[key[i]]
                __ i + 1 < l..(key):
                    cur.children[key[i+1]], delta = self.insert(cur, key, i + 1, val)
                ____:
                    delta = val - cur.val
                    cur.val = val

                cur.s.. += delta
                r.. cur, delta

        self.trie = Trie()

    ___ insert(self, key: s.., val: int) -> N..
        self.trie.insert(self.trie.root, key, 0, val)

    ___ s..(self, prefix: s..) -> int:
        node = self.trie.root
        ___ a __ prefix:
            __ a n.. __ node.children:
                r.. 0

            node = node.children[a]

        r.. node.s..


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
