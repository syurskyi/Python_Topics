#!/usr/bin/python3
"""
premium question
"""

____ t___ _______ L..
____ c.. _______ d..


c_ Solution:
    ___ wordsAbbreviation  words: L..[s..]) __ L..[s..]:
        """
        Sort the word, check prefix and last word

        Group by first and last char, group by prefix and last char
        then make a trie - hard to implement? TrieNode lambda

        Need to count the #appearances in the TrieNode
        """
        hm d..(l..)
        ret [N.. ___ _ __ words]
        ___ i, w __ e..(words
            hm[w[0], w[-1], l..(w)].a..(i)

        TrieNode l....: d..(TrieNode)

        ___ lst __ hm.v..
            root TrieNode()
            ___ i __ lst:
                w words[i]
                cur root
                ___ c __ w:
                    cur cur[c]
                    cur["count"] cur.g.. "count", 0) + 1

            ___ i __ lst:
                w words[i]
                prefix_l 0
                cur root
                ___ c __ w:
                    prefix_l += 1
                    cur cur[c]
                    __ cur["count"] __ 1:
                        _____

                ret[i] abbrev(w, prefix_l)

        r.. ret

    ___ abbrev  w, prefix_l
        abbrev_l l..(w) - 2 - prefix_l + 1
        __ abbrev_l > 1:
            r.. w[:prefix_l] + s..(abbrev_l) + w[-1]
        r.. w


__ _______ __ _______
    ... Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]) __ ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
