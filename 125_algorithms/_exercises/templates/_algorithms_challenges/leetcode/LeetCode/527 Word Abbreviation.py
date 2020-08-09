#!/usr/bin/python3
"""
premium question
"""

from typing ______ List
from collections ______ defaultdict


class Solution:
    ___ wordsAbbreviation(self, words: List[str]) -> List[str]:
        """
        Sort the word, check prefix and last word

        Group by first and last char, group by prefix and last char
        then make a trie - hard to implement? TrieNode lambda

        Need to count the #appearances in the TrieNode
        """
        hm = defaultdict(list)
        ret = [None ___ _ in words]
        ___ i, w in enumerate(words
            hm[w[0], w[-1], le.(w)].append(i)

        TrieNode = lambda: defaultdict(TrieNode)

        ___ lst in hm.values(
            root = TrieNode()
            ___ i in lst:
                w = words[i]
                cur = root
                ___ c in w:
                    cur = cur[c]
                    cur["count"] = cur.get("count", 0) + 1

            ___ i in lst:
                w = words[i]
                prefix_l = 0
                cur = root
                ___ c in w:
                    prefix_l += 1
                    cur = cur[c]
                    __ cur["count"] __ 1:
                        break

                ret[i] = self.abbrev(w, prefix_l)

        r_ ret

    ___ abbrev(self, w, prefix_l
        abbrev_l = le.(w) - 2 - prefix_l + 1
        __ abbrev_l > 1:
            r_ w[:prefix_l] + str(abbrev_l) + w[-1]
        r_ w


__ __name__ __ "__main__":
    assert Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]) __ ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
