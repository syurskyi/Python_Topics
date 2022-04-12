'''
Created on Aug 30, 2017

@author: MT
'''
c_ Solution(o..
    ___ matrixReshape  nums, r, c
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        __ n.. nums o. n.. nums[0]: r.. nums
        m, n l..(nums), l..(nums 0
        __ m*n !_ r*c:
            r.. nums
        res    # list
        k, l 0, 0
        ___ _ __ r..(r
            cur    # list
            ___ _ __ r..(c
                cur.a..(nums[k][l])
                l += 1
                __ l __ n:
                    l 0
                    k += 1
            res.a..(cur)
        r.. res
    
    ___ test
        testCases [
            [
                [[1, 2],
                 [3, 4]],
                1,
                4,
            ],
            [
                [[1, 2],
                 [3, 4]],
                2,
                4,
            ],
        ]
        ___ nums, r, c __ testCases:
            print('nums:')
            print('\n'.j..([s..(row) ___ row __ nums]
            print('r: %s' % r)
            print('c: %s' % c)
            result matrixReshape(nums, r, c)
            print('result:')
            print('\n'.j..([s..(row) ___ row __ result]
            print('-='*30)

__ _____ __ _____
    Solution().test()
