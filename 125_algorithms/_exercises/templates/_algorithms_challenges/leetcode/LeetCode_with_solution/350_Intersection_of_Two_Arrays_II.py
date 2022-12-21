c_ Solution o..
    ___ intersect  nums1, nums2
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.s..
        nums2.s..
        res =    # list
        pos1 = pos2 = 0
        w.. pos1 < l.. nums1) and pos2 < l.. nums2
            __ nums1[pos1] __ nums2[pos2]:
                res.append(nums1[pos1])
                pos1 += 1
                pos2 += 1
            ____ nums1[pos1] < nums2[pos2]:
                pos1 += 1
            ____
                pos2 += 1
        r_ res
