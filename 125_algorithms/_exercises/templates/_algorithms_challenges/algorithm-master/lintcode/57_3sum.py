class Solution:
    ___ threeSum(self, nums
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        __ not nums or le.(nums) < 3:
            r_ ans

        n = le.(nums)
        nums.sort()

        ___ a in range(n - 2
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            b, c = a + 1, n - 1

            w___ b < c:
                total = nums[a] + nums[b] + nums[c]

                __ total __ 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    w___ b < c and nums[b] __ nums[b - 1]:
                        b += 1
                    w___ b < c and nums[c] __ nums[c + 1]:
                        c -= 1
                ____ total < 0:
                    b += 1
                ____
                    c -= 1

        r_ ans
