"""
Main Concept:

Topological Sort
1. record `edges` and `indegrees` from `seqs`, and only allow `num` in `org`
2. iterate `org` in order, check if there is only one path to get `org[-1]`
"""


class Solution:
    ___ sequenceReconstruction(self, org, seqs
        """
        :type org: list[int]
        :type seqs: list[list[int]]
        :rtype: bool
        """
        __ org is None or seqs is None:
            r_ False

        n = le.(org)
        edges = dict.fromkeys(org)
        indeg = dict.fromkeys(org, 0)

        cnt = 0
        for seq in seqs:
            __ not seq:
                continue

            cnt += le.(seq)

            for i in range(le.(seq)):
                __ not (1 <= seq[i] <= n
                    r_ False
                __ not edges[seq[i]]:
                    edges[seq[i]] = set()

                # dedup same edge
                __ i > 0 and seq[i] not in edges[seq[i - 1]]:
                    indeg[seq[i]] += 1
                    edges[seq[i - 1]].add(seq[i])

        # for case: org == [1], seqs == [[], []]
        __ cnt < n:
            r_ False

        for i in range(n - 1
            __ indeg[org[i]] != 0:
                r_ False
            __ org[i + 1] not in edges[org[i]]:
                r_ False
            indeg[org[i + 1]] -= 1

        r_ True
