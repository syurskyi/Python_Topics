c_ Solution:
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        ans N..
        cnt 0

        ___ num __ nums:
            __ cnt __ 0:
                ans, cnt num, 1
            ____ ans __ ?
                cnt += 1
            ____
                cnt -_ 1

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
        N.. 0

        __ n.. nums:
            r.. N..

        freq    # dict

        ___ a __ nums:
            freq[a] freq.g.. a, 0) + 1

        ___ a, cnt __ freq.i..
            __ cnt > l..(nums) // 2:
                r.. a

        r.. N..
