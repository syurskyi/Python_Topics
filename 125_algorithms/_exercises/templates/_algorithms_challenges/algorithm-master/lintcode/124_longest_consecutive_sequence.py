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

        __ n.. nums:
            r.. ans

        cands = set(nums)  # dedup

        ___ a __ nums:
            __ a n.. __ cands:
                continue

            cands.discard(a)
            size = 1
            b, c = a - 1, a + 1

            w.... b __ cands:
                cands.discard(b)
                b -= 1
                size += 1

            w.... c __ cands:
                cands.discard(c)
                c += 1
                size += 1

            __ size > ans:
                ans = size

        r.. ans


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

        __ n.. nums:
            r.. ans

        nums.s..()

        size = 1

        ___ i __ r..(1, l..(nums)):
            __ nums[i] __ nums[i - 1]:
                continue

            __ nums[i] __ nums[i - 1] + 1:
                size += 1
            ____:
                size = 1

            __ size > ans:
                ans = size

        r.. ans __ ans > 0 ____ size
