"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
__author__ = 'Daniel'


c_ Solution(o..):
    ___ wiggleSort  A):
        """
        1. Quick selection for finding median (Average O(n))
        2. Three-way partitioning to split the data
        3. Re-mapping the index to do in-place partitioning
        Average time O(n)
        Space O(1)
        :type A: List[int]
        :rtype: in-place
        """
        n = l..(A)
        median_idx = find_kth(A, 0, n, n/2)
        v = A[median_idx]

        idx = l.... i: (2*i+1) % (n|1)
        lt = -1
        hi = n
        i = 0
        w.... i < hi:
            __ A[idx(i)] > v:
                lt += 1
                A[idx(lt)], A[idx(i)] = A[idx(i)], A[idx(lt)]
                i += 1
            ____ A[idx(i)] __ v:
                i += 1
            ____:
                hi -= 1
                A[idx(hi)], A[idx(i)] = A[idx(i)], A[idx(hi)]

    ___ pivot  A, lo, hi, pidx_ N..
        lt = lo-1
        gt = hi
        __ n.. pidx: pidx = lo

        v = A[pidx]
        i = lo
        w.... i < gt:
            __ A[i] < v:
                lt += 1
                A[lt], A[i] = A[i], A[lt]
                i += 1
            ____ A[i] __ v:
                i += 1
            ____:
                gt -= 1
                A[gt], A[i] = A[i], A[gt]

        r.. lt, gt

    ___ find_kth  A, lo, hi, k):
        __ lo >= hi: r..

        lt, gt = pivot(A, lo, hi)

        __ lt < k < gt:
            r.. k
        __ k <= lt:
            r.. find_kth(A, lo, lt+1, k)
        ____:
            r.. find_kth(A, gt, hi, k)


c_ SolutionSort(o..):
    ___ wiggleSort  nums):
        """
        Sort-based: interleave the small half and large half

        Could they be "equal to"? That would require some number M to appear both in the smaller and the larger half.
        It shall be the largest in the smaller half and the smallest in the larger half.

        To deal with duplicate median element cases (e.g. [4 5 5 6]), interleave in a reverse order
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = l..(nums)
        A = s..(nums)

        j, k = (n-1) / 2, n-1
        ___ i __ x..(l..(nums)):
            __ i % 2 __ 0:
                nums[i] = A[j]
                j -= 1
            ____:
                nums[i] = A[k]
                k -= 1


__ _______ __ _______
    # A = [1, 5, 1, 1, 6, 4]
    A = [3, 2, 1, 1, 3, 2]
    Solution().wiggleSort(A)
    print A
