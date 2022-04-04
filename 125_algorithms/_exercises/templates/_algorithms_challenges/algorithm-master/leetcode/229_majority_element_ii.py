c_ Solution:
    ___ majorityElement  nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans    # list

        __ n.. nums:
            r.. []

        a1  a2  N..
        c1  c2  0

        ___ num __ nums:
            __ a1 __ num:
                c1 + 1
            ____ a2 __ num:
                c2 + 1
            ____ c1 __ 0:
                a1, c1  num, 1
            ____ c2 __ 0:
                a2, c2  num, 1
            ____:
                c1 - 1
                c2 - 1

        c1  c2  0

        ___ num __ nums:
            __ num __ a1:
                c1 + 1
            ____ num __ a2:
                c2 + 1

        ___ a, c __ ((a1, c1), (a2, c2:
            __ c > l..(nums) // 3:
                ans.a..(a)

        r.. ans
