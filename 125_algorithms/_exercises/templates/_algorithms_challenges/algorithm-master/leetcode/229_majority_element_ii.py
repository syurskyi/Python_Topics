class Solution:
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        __ not nums:
            r_ []

        a1 = a2 = None
        c1 = c2 = 0

        for num in nums:
            __ a1 __ num:
                c1 += 1
            ____ a2 __ num:
                c2 += 1
            ____ c1 __ 0:
                a1, c1 = num, 1
            ____ c2 __ 0:
                a2, c2 = num, 1
            ____
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0

        for num in nums:
            __ num __ a1:
                c1 += 1
            ____ num __ a2:
                c2 += 1

        for a, c in ((a1, c1), (a2, c2)):
            __ c > le.(nums) // 3:
                ans.append(a)

        r_ ans
