class Solution:
    ___ findMissing(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            r_ 0

        ans = n = le.(nums)

        ___ i in range(n
            ans ^= i ^ nums[i]

        r_ ans


class Solution:
    ___ findMissing(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            r_ 0

        nums.sort()

        ___ i in range(le.(nums)):
            __ i != nums[i]:
                r_ i

        r_ i + 1
