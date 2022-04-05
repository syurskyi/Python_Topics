c_ Solution:
    ___ threeSumClosest  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        __ n.. nums o. l..(nums) < 3 o. target __ N..
            r.. -1

        ans = INF = f__('inf')
        n = l..(nums)
        nums.s..()

        ___ a __ r..(n - 2
            __ a > 0 a.. nums[a] __ nums[a - 1]:
                _____

            b, c = a + 1, n - 1

            w.... b < c:
                total = nums[a] + nums[b] + nums[c]

                __ total __ target:
                    r.. total

                __ a..(total - target) < a..(ans - target
                    ans = total

                __ total < target:
                    b += 1
                ____
                    c -_ 1

        r.. ans __ ans < INF ____ -1
