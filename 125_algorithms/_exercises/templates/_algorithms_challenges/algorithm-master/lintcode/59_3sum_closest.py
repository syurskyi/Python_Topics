class Solution:
    ___ threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums o. l..(nums) < 3 o. target __ N..
            r.. -1

        ans = INF = float('inf')
        n = l..(nums)
        nums.sort()

        ___ a __ r..(n - 2):
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            b, c = a + 1, n - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                __ total __ target:
                    r.. total

                __ abs(total - target) < abs(ans - target):
                    ans = total

                __ total < target:
                    b += 1
                ____:
                    c -= 1

        r.. ans __ ans < INF ____ -1
