"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate
between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with
fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and
negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two
differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is
obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining
elements in their original order.
"""
__author__ = 'Daniel'


c_ Solution(o..
    ___ wiggleMaxLength  A
        """
        Let H[i] be max wiggle length for [0, i] with A[i] as high point
        Let L[i] be similarly defined but as low point.

        Consider A[i] > A[i-1]:
          H[i] = L[i-1] + 1 # wiggle up
          L[i] = L[i-1]  #
        A[i] < A[i-1] case has similar formula

          H[i] = H[i-1]
               = L[i-1] + 1

          L[i] = L[i-1]
               = H[i-1] + 1

        Therefore, max(H[i], L[i]) are monotonously non-decreasing  (rather than H[i] or L[i] monotonously
        non-decreasing separately.
        O(n)

        Additionally, possibly space optimized to O(1) by reusing space
        :type A: List[int]
        :rtype: int
        """
        __ n.. A: r.. 0
        N = l..(A)
        H = [1 ___ _ __ x..(N)]
        L = [1 ___ _ __ x..(N)]
        ___ i __ x..(1, N
            L[i] = H[i-1] + 1 __ A[i] < A[i-1] ____ L[i-1]
            H[i] = L[i-1] + 1 __ A[i] > A[i-1] ____ H[i-1]

        r.. m..(H[N-1], L[N-1])

    ___ wiggleMaxLengthSuboptimal  A
        """
        Let H[i] be wiggle length ends at i, with A[i] as high point
        Let L[i] be similarly defined but as low point.
        O(n^2)
        :type A: List[int]
        :rtype: int
        """
        __ n.. A: r.. 0

        N = l..(A)
        H = [1 ___ _ __ x..(N)]
        L = [1 ___ _ __ x..(N)]
        gmax = 1
        ___ i __ x..(1, N
            ___ j __ x..(i
                __ A[i] > A[j]:
                    H[i] = m..(H[i], L[j] + 1)
                ____ A[i] < A[j]:
                    L[i] = m..(L[i], H[j] + 1)

                gmax = m..(gmax, H[i], L[i])

        r.. gmax
