#!/usr/bin/python3
"""
premium question
"""

____ typing _______ List
____ c.. _______ defaultdict


c_ Solution:
    ___ wordsAbbreviation(self, words: List[s..]) __ List[s..]:
        """
        Sort the word, check prefix and last word

        Group by first and last char, group by prefix and last char
        then make a trie - hard to implement? TrieNode lambda

        Need to count the #appearances in the TrieNode
        """
        hm = defaultdict(l..)
        ret = [N.. ___ _ __ words]
        ___ i, w __ e..(words):
            hm[w[0], w[-1], l..(w)].a..(i)

        TrieNode = l....: defaultdict(TrieNode)

        ___ lst __ hm.v..
            root = TrieNode()
            ___ i __ lst:
                w = words[i]
                cur = root
                ___ c __ w:
                    cur = cur[c]
                    cur["count"] = cur.get("count", 0) + 1

            ___ i __ lst:
                w = words[i]
                prefix_l = 0
                cur = root
                ___ c __ w:
                    prefix_l += 1
                    cur = cur[c]
                    __ cur["count"] __ 1:
                        break

                ret[i] = abbrev(w, prefix_l)

        r.. ret

    ___ abbrev(self, w, prefix_l):
        abbrev_l = l..(w) - 2 - prefix_l + 1
        __ abbrev_l > 1:
            r.. w[:prefix_l] + s..(abbrev_l) + w[-1]
        r.. w


__ __name__ __ "__main__":
    ... Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]) __ ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
