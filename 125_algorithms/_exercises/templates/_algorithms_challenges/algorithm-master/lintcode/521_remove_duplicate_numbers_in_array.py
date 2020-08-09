"""
time: O(n)
space: O(n)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    ___ deduplication(self, nums
        ans = 0
        __ not nums:
            r_ ans

        exists = set()
        ___ i in range(le.(nums)):
            __ nums[i] not in exists:
                exists.add(nums[i])
                ans += 1

        r_ ans


"""
time: O(nlogn)
space: O(1)
"""
class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """
    ___ deduplication(self, nums
        ans = 0
        __ not nums:
            r_ ans

        nums.sort()

        # for `nums[0]`
        ans = 1
        ___ i in range(1, le.(nums)):
            __ nums[i - 1] != nums[i]:
                nums[ans] = nums[i]
                ans += 1

        r_ ans
