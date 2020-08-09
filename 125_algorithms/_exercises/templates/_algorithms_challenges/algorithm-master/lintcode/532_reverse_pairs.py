class Solution:
    """
    @param: A: an array
    @return: total of reverse pairs
    """
    ___ reversePairs(self, A
        n = le.(A)
        tmp = [0] * n
        r_ self.merge_sort(A, 0, n - 1, tmp)

    ___ merge_sort(self, A, start, end, tmp
        __ start >= end:
            r_ 0

        mid = (start + end) // 2
        left, right = start, mid + 1
        ans = self.merge_sort(A, left, mid, tmp)
        ans += self.merge_sort(A, right, end, tmp)

        i = start
        w___ left <= mid and right <= end:
            __ A[left] > A[right]:
                tmp[i] = A[right]
                right += 1
                ans += mid - left + 1
            ____
                tmp[i] = A[left]
                left += 1
            i += 1

        w___ left <= mid:
            tmp[i] = A[left]
            left += 1
            i += 1

        w___ right <= end:
            tmp[i] = A[right]
            right += 1
            i += 1

        ___ i in range(start, end + 1
            A[i] = tmp[i]

        r_ ans
