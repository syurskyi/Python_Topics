class Solution:
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            r_ 0

        ans = None
        cnt = 0

        for num in nums:
            __ cnt __ 0:
                ans, cnt = num, 1
            ____ ans __ num:
                cnt += 1
            ____
                cnt -= 1

        r_ ans


class Solution:
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            r_ 0

        nums.sort()

        r_ nums[le.(nums) // 2]


class Solution:
    ___ majorityElement(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        NOT_FOUND = 0

        __ not nums:
            r_ NOT_FOUND

        freq = {}

        for a in nums:
            freq[a] = freq.get(a, 0) + 1

        for a, cnt in freq.items(
            __ cnt > le.(nums) // 2:
                r_ a

        r_ NOT_FOUND
