"""
Main Concept:

Topological Sort
1. record `edges` and `indegrees` from `seqs`, and only allow `num` in `org`
2. iterate `org` in order, check if there is only one path to get `org[-1]`
"""


c_ Solution:
    ___ sequenceReconstruction  org, seqs):
        """
        :type org: list[int]
        :type seqs: list[list[int]]
        :rtype: bool
        """
        __ org __ N.. o. seqs __ N..
            r.. F..

        n = l..(org)
        edges = d...f..(org)
        indeg = d...f..(org, 0)

        cnt = 0
        ___ seq __ seqs:
            __ n.. seq:
                _____

            cnt += l..(seq)

            ___ i __ r..(l..(seq)):
                __ n.. (1 <= seq[i] <= n):
                    r.. F..
                __ n.. edges[seq[i]]:
                    edges[seq[i]] = s..()

                # dedup same edge
                __ i > 0 a.. seq[i] n.. __ edges[seq[i - 1]]:
                    indeg[seq[i]] += 1
                    edges[seq[i - 1]].add(seq[i])

        # for case: org == [1], seqs == [[], []]
        __ cnt < n:
            r.. F..

        ___ i __ r..(n - 1):
            __ indeg[org[i]] != 0:
                r.. F..
            __ org[i + 1] n.. __ edges[org[i]]:
                r.. F..
            indeg[org[i + 1]] -= 1

        r.. T..
