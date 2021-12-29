#!/usr/bin/python3
"""
A gene string can be represented by an 8-character long string, with choices
from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to
"end"), where ONE mutation is defined as ONE single character changed in the
gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the
minimum number of mutations needed to mutate from "start" to "end". If there is
no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be
valid.
You may assume start and end string is not the same.
"""


class Solution:
    ___ is_neighbor(self, p, q):
        diff = 0
        ___ a, b __ zip(p, q):
            __ a != b:
                diff += 1
            __ diff > 1:
                r.. False
        r.. True

    ___ minMutation(self, start, end, bank):
        """
        BFS, record level and avoid loop

        Similar to 127 Word Ladder

        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        q = [start]
        visited = {start}
        lvl = 0
        while q:
            cur_q    # list
            ___ e __ q:
                __ e __ end:
                    r.. lvl
                ___ t __ bank:
                    __ t n.. __ visited and self.is_neighbor(e, t):
                        visited.add(t)
                        cur_q.a..(t)

            lvl += 1
            q = cur_q

        r.. -1


__ __name__ __ "__main__":
    ... Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]) __ -1
    ... Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) __ 2
