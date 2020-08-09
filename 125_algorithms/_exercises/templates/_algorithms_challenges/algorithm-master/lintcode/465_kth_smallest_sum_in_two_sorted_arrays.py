______ heapq

"""
Assuming: le.(A) == le.(B) == 3

To find the result(min of A[i]+B[j]), we got a 3x3 matrix:
AB | 0 | 1 | 2 |
 0 | a | b | c |
 1 | d | e | f |
 2 | g | h | i |

 1. put the first column (0, j) into heap, these child is the min for each row
 2. get the minest one, and move the `x` pointer forward, put the child at (x+1, y)
 3. keep find the minest one in current heap, then we can find the kth child
"""

class Solution:

    """
    @param: A: an integer arrays sorted in ascending order
    @param: B: an integer arrays sorted in ascending order
    @param: k: An integer
    @return: An integer
    """
    ___ kthSmallestSum(self, A, B, k
        m, n = le.(A), le.(B)
        ans = j = 0
        heap = []
        for i in range(min(m, k)): heapq.heappush(heap, (A[i] + B[0], i, 0))
        w___ k > 0:
            ans = heapq.heappop(heap)
            j = ans[2] + 1
            __ j < n:
                heapq.heappush(heap, (A[ans[1]] + B[j], ans[1], j))
            k -= 1
        r_ ans[0]
