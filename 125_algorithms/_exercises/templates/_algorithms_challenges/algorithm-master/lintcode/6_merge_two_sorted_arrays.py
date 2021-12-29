class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    ___ mergeSortedArray(self, A, B):
        __ n.. A:
            r.. B
        __ n.. B:
            r.. A

        m, n = l..(A), l..(B)
        ans = [0] * (m + n)

        i = j = index = 0
        w.... i < m a.. j < n:
            __ A[i] < B[j]:
                ans[index] = A[i]
                i += 1
            ____:
                ans[index] = B[j]
                j += 1
            index += 1

        w.... i < m:
            ans[index] = A[i]
            i += 1
            index += 1

        w.... j < n:
            ans[index] = B[j]
            j += 1
            index += 1

        r.. ans
