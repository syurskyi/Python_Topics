_______ h__

"""
Assuming: len(A) == len(B) == 3

To find the result(min of A[i]+B[j]), we got a 3x3 matrix:
AB | 0 | 1 | 2 |
 0 | a | b | c |
 1 | d | e | f |
 2 | g | h | i |

 1. put the first column (0, j) into heap, these child is the min for each row
 2. get the minest one, and move the `x` pointer forward, put the child at (x+1, y)
 3. keep find the minest one in current heap, then we can find the kth child
"""

c_ Solution:

    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    ___ kthSmallestSum  A, B, k
        m, n l..(A), l..(B)
        ans j 0
        heap    # list
        ___ i __ r..(m..(m, k: h__.heappush(heap, (A[i] + B[0], i, 0
        w.... k > 0
            ans h__.heappop(heap)
            j ans[2] + 1
            __ j < n:
                h__.heappush(heap, (A[ans[1]] + B[j], ans[1], j
            k -_ 1
        r.. ans[0]
