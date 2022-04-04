c_ Solution:
    """
    @param: A: an array
    @return: total of reverse pairs
    """
    ___ reversePairs  A
        n = l..(A)
        tmp = [0] * n
        r.. merge_sort(A, 0, n - 1, tmp)

    ___ merge_sort  A, start, end, tmp
        __ start >= end:
            r.. 0

        mid = (start + end) // 2
        left, right = start, mid + 1
        ans = merge_sort(A, left, mid, tmp)
        ans += merge_sort(A, right, end, tmp)

        i = start
        w.... left <= mid a.. right <= end:
            __ A[left] > A[right]:
                tmp[i] = A[right]
                right += 1
                ans += mid - left + 1
            ____
                tmp[i] = A[left]
                left += 1
            i += 1

        w.... left <= mid:
            tmp[i] = A[left]
            left += 1
            i += 1

        w.... right <= end:
            tmp[i] = A[right]
            right += 1
            i += 1

        ___ i __ r..(start, end + 1
            A[i] = tmp[i]

        r.. ans
