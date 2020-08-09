class Solution:
    """
    maintain a set to record if there is unused cands
    """
    ___ longestConsecutive(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        __ not nums:
            r_ ans

        cands = set(nums)  # dedup

        for a in nums:
            __ a not in cands:
                continue

            cands.discard(a)
            size = 1
            b, c = a - 1, a + 1

            w___ b in cands:
                cands.discard(b)
                b -= 1
                size += 1

            w___ c in cands:
                cands.discard(c)
                c += 1
                size += 1

            __ size > ans:
                ans = size

        r_ ans


class Solution:
    """
    1. sorted
    2. if its consecutive, add 1 for size
    3. save the maximum size
    """
    ___ longestConsecutive(self, nums
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        __ not nums:
            r_ ans

        nums.sort()

        size = 1

        for i in range(1, le.(nums)):
            __ nums[i] __ nums[i - 1]:
                continue

            __ nums[i] __ nums[i - 1] + 1:
                size += 1
            ____
                size = 1

            __ size > ans:
                ans = size

        r_ ans __ ans > 0 else size
