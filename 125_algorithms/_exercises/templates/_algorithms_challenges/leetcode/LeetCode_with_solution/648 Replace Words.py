#!/usr/bin/python3
"""
In English, we have a concept called root, which can be followed by some other
words to form another longer word - let's call this word successor. For example,
the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to
replace all the successor in the sentence with the root forming it. If a
successor has many roots can form it, replace it with the root with the shortest
length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
____ t___ _______ L..
____ c.. _______ d..


c_ Node:
    ___ - , chr
        chr chr
        ended F..
        children d..(l....: N..)


c_ Trie:
    ___ -
        root Node(N..)  # dummy

    ??
    ___ i.. cls, node, w, i
        __ n.. node:
            node Node(w[i])

        __ i __ l..(w) - 1:
            node.ended T..
        ____
            nxt w[i + 1]
            node.children[nxt]  ?.i.. node.children[nxt], w, i + 1)

        r.. node

    ??
    ___ s..(cls, node, w, i
        __ n.. node:
            r..

        __ node.chr !_ w[i]:
            r..

        __ node.ended:
            r.. w[:i+1]
        ____ i + 1 < l..(w
            r..  ?.s..(node.children[w[i + 1]], w, i + 1)
        ____
            r..

c_ Solution:
    ___ replaceWords  dic: L..[s..], sentence: s..) __ s..
        trie Trie()
        ___ word __ dic:
            root trie.root
            root.children[word[0]] Trie.i.. root.children[word[0]], word, 0)

        ret    # list
        ___ word __ sentence.s..(" "
            ___ child __ trie.root.children.v..
                searched Trie.s..(child, word, 0)
                __ searched:
                    ret.a..(searched)
                    _____
            ____
                ret.a..(word)

        r.. " ".j..(ret)


__ _______ __ _______
    ... Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") __ "the cat was rat by the bat"
