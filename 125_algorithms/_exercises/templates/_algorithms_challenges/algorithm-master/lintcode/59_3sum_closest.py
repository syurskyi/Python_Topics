class Solution:
    ___ threeSumClosest(self, nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ not nums or le.(nums) < 3 or target is None:
            r_ -1

        ans = INF = float('inf')
        n = le.(nums)
        nums.sort()

        ___ a in range(n - 2
            __ a > 0 and nums[a] __ nums[a - 1]:
                continue

            b, c = a + 1, n - 1

            w___ b < c:
                total = nums[a] + nums[b] + nums[c]

                __ total __ target:
                    r_ total

                __ abs(total - target) < abs(ans - target
                    ans = total

                __ total < target:
                    b += 1
                ____
                    c -= 1

        r_ ans __ ans < INF else -1
