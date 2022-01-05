#!/usr/bin/python3
"""
Given a list of words, we may encode it by writing a reference string S and a
list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as
S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference
string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the
given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
"""
____ typing _______ List


c_ Solution:
    ___ minimumLengthEncoding  words: List[s..]) __ i..:
        """
        suffix trie
        only suffix matters

        fast trie with dict
        """
        root    # dict
        ends    # list
        ___ word __ set(words):
            cur = root
            ___ c __ word[::-1]:
                nxt = cur.get(c, {})
                cur[c] = nxt
                cur = nxt

            ends.a..((cur, l..(word)))

        r.. s..(
            l + 1
            ___ node, l __ ends
            __ l..(node) __ 0  # no child
        )


__ _______ __ _______
    ... Solution().minimumLengthEncoding(["time", "me", "bell"]) __ 10
