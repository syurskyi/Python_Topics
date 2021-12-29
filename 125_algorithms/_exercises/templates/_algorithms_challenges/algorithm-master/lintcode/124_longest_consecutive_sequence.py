class Solution:
    """
    maintain a set to record if there is unused cands
    """
    ___ longestConsecutive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        __ not nums:
            return ans

        cands = set(nums)  # dedup

        for a in nums:
            __ a not in cands:
                continue

            cands.discard(a)
            size = 1
            b, c = a - 1, a + 1

            while b in cands:
                cands.discard(b)
                b -= 1
                size += 1

            while c in cands:
                cands.discard(c)
                c += 1
                size += 1

            __ size > ans:
                ans = size

        return ans


class Solution:
    """
    1. sorted
    2. if its consecutive, add 1 for size
    3. save the maximum size
    """
    ___ longestConsecutive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        __ not nums:
            return ans

        nums.sort()

        size = 1

        for i in range(1, len(nums)):
            __ nums[i] == nums[i - 1]:
                continue

            __ nums[i] == nums[i - 1] + 1:
                size += 1
            else:
                size = 1

            __ size > ans:
                ans = size

        return ans __ ans > 0 else size
