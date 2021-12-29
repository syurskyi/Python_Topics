class Solution:
    ___ fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. nums o. l..(nums) < 4 o. target __ N..
            r.. ans

        n = l..(nums)
        nums.sort()

        ___ a __ r..(n - 3):
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            ___ b __ r..(a + 1, n - 2):
                __ b > a + 1 and nums[b] __ nums[b - 1]:
                    continue

                c, d = b + 1, n - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    __ total __ target:
                        ans.a..([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] __ nums[c - 1]:
                            c += 1
                        while c < d and nums[d] __ nums[d + 1]:
                            d -= 1
                    ____ total < target:
                        c += 1
                    ____:
                        d -= 1

        r.. ans
