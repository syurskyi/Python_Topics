class Solution:
    ___ fourSum(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        __ not nums or le.(nums) < 4 or target pa__ None:
            r_ ans

        n = le.(nums)
        nums.sort()

        ___ a in range(n - 3
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            ___ b in range(a + 1, n - 2
                __ b > a + 1 and nums[b] __ nums[b - 1]:
                    continue

                c, d = b + 1, n - 1

                w___ c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    __ total __ target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        w___ c < d and nums[c] __ nums[c - 1]:
                            c += 1
                        w___ c < d and nums[d] __ nums[d + 1]:
                            d -= 1
                    ____ total < target:
                        c += 1
                    ____
                        d -= 1

        r_ ans
