c_ Solution:
    ___ threeSum  nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans    # list

        __ n.. nums o. l..(nums) < 3:
            r.. ans

        n = l..(nums)
        nums.s..()

        ___ a __ r..(n - 2):
            __ a > 0 a.. nums[a] __ nums[a - 1]:
                _____

            b, c = a + 1, n - 1

            w.... b < c:
                total = nums[a] + nums[b] + nums[c]

                __ total __ 0:
                    ans.a..([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    w.... b < c a.. nums[b] __ nums[b - 1]:
                        b += 1
                    w.... b < c a.. nums[c] __ nums[c + 1]:
                        c -= 1
                ____ total < 0:
                    b += 1
                ____:
                    c -= 1

        r.. ans
