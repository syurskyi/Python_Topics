class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    ___ mergeSortedArray(self, A, B
        __ not A:
            r_ B
        __ not B:
            r_ A

        m, n = le.(A), le.(B)
        ans = [0] * (m + n)

        i = j = index = 0
        w___ i < m and j < n:
            __ A[i] < B[j]:
                ans[index] = A[i]
                i += 1
            ____
                ans[index] = B[j]
                j += 1
            index += 1

        w___ i < m:
            ans[index] = A[i]
            i += 1
            index += 1

        w___ j < n:
            ans[index] = B[j]
            j += 1
            index += 1

        r_ ans
