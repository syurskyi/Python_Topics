#!/usr/bin/python3
"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to
build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify
exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
"""
____ typing _______ List
____ c.. _______ defaultdict


c_ MagicDictionary:

    ___ - ):
        """
        Initialize your data structure here.
        """
        c_ Node:
            ___ - , chr):
                chr = chr
                end = F..  # a word ends here
                children = defaultdict(l....: N..)

        c_ Trie:
            ___ - ):
                root = Node(N..)

            ___ insert  cur, s, i):
                __ n.. cur:
                    cur = Node(s[i])

                __ i __ l..(s) -1:
                    cur.end = T..
                ____:
                    nxt = s[i+1]
                    cur.children[nxt] = insert(cur.children[nxt], s, i + 1)

                r.. cur

            ___ s..  cur, s, i, modified):
                __ cur.chr != s[i]:
                    __ modified:
                        r.. F..
                    modified = T..

                __ i __ l..(s) - 1:
                    # modified exactly once and have a word ends here 
                    r.. modified a.. cur.end

                ___ child __ cur.children.v..
                    __ s..(child, s, i + 1, modified):
                        r.. T..

                r.. F..

        trie = Trie()

    ___ buildDict  dic: List[s..]) __ N..
        """
        Build a dictionary through a list of words
        """
        ___ s __ dic:
            root = trie.root
            root.children[s[0]] = trie.insert(root.children[s[0]], s, 0)

    ___ s..  word: s..) __ b..:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        ___ child __ trie.root.children.v..
            __ trie.s..(child, word, 0, F..):
                r.. T..

        r.. F..


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
