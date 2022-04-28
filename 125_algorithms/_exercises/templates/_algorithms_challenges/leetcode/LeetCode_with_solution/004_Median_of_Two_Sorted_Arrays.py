c_ Solution o..
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     p1 = p2 = 0
    #     ls1 = len(nums1)
    #     ls2 = len(nums2)
    #     all_nums = []
    #     median = 0.0
    #     while p1 < ls1 and p2 < ls2:
    #         if nums1[p1] < nums2[p2]:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #         else:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     if p1 < ls1:
    #         while p1 < ls1:
    #             all_nums.append(nums1[p1])
    #             p1 += 1
    #     if p2 < ls2:
    #         while p2 < ls2:
    #             all_nums.append(nums2[p2])
    #             p2 += 1
    #     # print all_nums
    #     if (ls1 + ls2) % 2 == 1:
    #         median = all_nums[(ls1 + ls2) / 2]
    #     else:
    #         median = 1.0 * (all_nums[(ls1 + ls2) / 2] + all_nums[(ls1 + ls2) / 2 - 1]) / 2
    #     return median

    ___ findMedianSortedArrays  nums1 nums2
        # https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
        # https://discuss.leetcode.com/topic/16797/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation
        ls1, ls2  l.. ? l.. ?
        __ ? < ?
            r_ ? ? ?
        l, r _ 0 _2 * 2
        w.. ? <_ ?
            mid2  ? + ? >> 1
            mid1  _1 + _2 - ?
            L1  -sys.m.. - 1 __ mid1 __ 0 ____ nums1[(mid1 - 1) >> 1
            L2  -sys.m.. - 1 __ mid2 __ 0 ____ nums2[(mid2 - 1) >> 1
            R1  sys.m.. __ mid1 __ 2 * ls1 ____ nums1[mid1 >> 1]
            R2  sys.m.. __ mid2 __ 2 * ls2 ____ nums2[mid2 >> 1]
            __ L1 > R2:
                l = mid2 + 1
            ____ L2 > R1:
                r = mid2 - 1
            ____
                r_ (max(L1, L2) + min(R1, R2)) / 2.0


__ ____ __ ____
    # begin
    s  ?
    print s.findMedianSortedArrays([1, 1], [1, 2])
