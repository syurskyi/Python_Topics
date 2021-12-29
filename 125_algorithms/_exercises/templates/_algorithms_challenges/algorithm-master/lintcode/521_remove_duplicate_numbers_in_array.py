"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    ___ deduplication(self, nums):
        ans = 0
        __ n.. nums:
            r.. ans

        exists = set()
        ___ i __ r..(l..(nums)):
            __ nums[i] n.. __ exists:
                exists.add(nums[i])
                ans += 1

        r.. ans


"""
time: O(nlogn)
space: O(1)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    ___ deduplication(self, nums):
        ans = 0
        __ n.. nums:
            r.. ans

        nums.sort()

        # for `nums[0]`
        ans = 1
        ___ i __ r..(1, l..(nums)):
            __ nums[i - 1] != nums[i]:
                nums[ans] = nums[i]
                ans += 1

        r.. ans
