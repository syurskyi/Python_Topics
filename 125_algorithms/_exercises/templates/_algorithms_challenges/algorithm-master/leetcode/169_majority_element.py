c_ Solution:
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        ans = N..
        cnt = 0

        ___ num __ nums:
            __ cnt __ 0:
                ans, cnt = num, 1
            ____ ans __ num:
                cnt += 1
            ____:
                cnt -= 1

        r.. ans


c_ Solution:
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        nums.s..()

        r.. nums[l..(nums) // 2]


c_ Solution:
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        NOT_FOUND = 0

        __ n.. nums:
            r.. NOT_FOUND

        freq    # dict

        ___ a __ nums:
            freq[a] = freq.g.. a, 0) + 1

        ___ a, cnt __ freq.i..:
            __ cnt > l..(nums) // 2:
                r.. a

        r.. NOT_FOUND
