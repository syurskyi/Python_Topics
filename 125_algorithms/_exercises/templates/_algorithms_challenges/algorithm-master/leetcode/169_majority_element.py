class Solution:
    ___ majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            return 0

        ans = None
        cnt = 0

        for num in nums:
            __ cnt == 0:
                ans, cnt = num, 1
            elif ans == num:
                cnt += 1
            else:
                cnt -= 1

        return ans


class Solution:
    ___ majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ not nums:
            return 0

        nums.sort()

        return nums[len(nums) // 2]


class Solution:
    ___ majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NOT_FOUND = 0

        __ not nums:
            return NOT_FOUND

        freq = {}

        for a in nums:
            freq[a] = freq.get(a, 0) + 1

        for a, cnt in freq.items():
            __ cnt > len(nums) // 2:
                return a

        return NOT_FOUND
