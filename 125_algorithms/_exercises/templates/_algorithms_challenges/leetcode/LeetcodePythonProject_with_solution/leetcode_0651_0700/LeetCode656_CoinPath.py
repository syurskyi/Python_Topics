'''
Created on Oct 5, 2017

@author: MT
'''
c_ Solution(o..):
    ___ cheapestJump  A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        nums = A
        __ n.. nums o. nums[-1] __ -1: r.. []
        res    # list
        n = l..(nums)
        dp = [float('inf')]*n
        dp[-1] = nums[-1]
        pos = [-1]*n
        ___ i __ r..(n-2, -1, -1):
            __ nums[i] __ -1:
                _____
            ___ j __ r..(i+1, m..(i+B, n-1)+1):
                __ dp[j] __ float('inf'):
                    _____
                __ nums[i]+dp[j] < dp[i]:
                    dp[i] = nums[i]+dp[j]
                    pos[i] = j
        __ dp[0] __ float('inf'):
            r.. res
        ind = 0
        w.... ind != -1:
            res.a..(ind+1)
            ind = pos[ind]
        r.. res
    
    ___ test
        testCases = [
            [
                [1, 2, 4, -1, 2],
                2,
            ],
            [
                [1, 2, 4, -1, 2],
                1
            ],
            [
                [0, 0, 0, 0, 0, 0],
                3,
            ],
        ]
        ___ a, b __ testCases:
            print('a: %s' % a)
            print('b: %s' % b)
            result = cheapestJump(a, b)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
