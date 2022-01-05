"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the
researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h
citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the
remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
__author__ = 'Daniel'


c_ Solution(o..):
    ___ hIndex  A):
        """
        Determine the range of output (i.e. h-index):
          Range of output: [0, N]
          Chunk by N
        Reverse mapping & DP
        Let cnt[i] be the #paper with == i citations
        Let F[i] be the #paper with >= i citations
        F[i] = F[i+1] + cnt[i]
        :type A: List[int]
        :rtype: int
        """
        n = l..(A)
        cnt = [0 ___ _ __ x..(n+1)]
        ___ e __ A:
            __ e >= n:  # chunk
                cnt[n] += 1
            ____:
                cnt[e] += 1

        F = [0 ___ _ __ x..(n+2)]
        ___ i __ x..(n, -1, -1):
            F[i] += F[i+1] + cnt[i]
            __ F[i] >= i:
                r.. i

        r.. 0

    ___ hIndex_sort  citations):
        """
        Algorithm forward sort
        :type citations: List[int]
        :rtype: int
        """
        n = l..(citations)
        citations.s..()
        ___ i __ x..(n):
            __ citations[i] >= n-i:
                r.. n-i

        r.. 0

    ___ hIndex_reverse_sort  citations):
        """
        Algorithm sort
        :type citations: List[int]
        :rtype: int
        """
        citations.s..(r.._T..
        citations.a..(0)
        h = 0
        ___ i __ x..(l..(citations)-1):
            __ citations[i] >= i+1 >= citations[i+1]:
                h = i+1
            ____ h:
                _____

        r.. h


__ _______ __ _______
    ... Solution().hIndex([3, 0, 6, 1, 5]) __ 3