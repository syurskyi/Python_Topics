'''
Created on May 6, 2017

@author: MT
'''

c_ Solution(o..
    ___ PredictTheWinner  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = l..(nums)
        dp = [[0]*n ___ _ __ r..(n)]
        ___ i __ r..(n
            dp[i][i] = nums[i]
        ___ l __ r..(1, n
            ___ i __ r..(n-l
                j = i+l
                dp[i][j] = m..(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        r.. dp[0][n-1] >_ 0
    
    ___ PredictTheWinner_DnC  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem    # dict
        r.. helper(nums, 0, l..(nums)-1) >_ 0
    
    ___ helper  nums, start, end
        n = l..(nums)
        num = start*n+end
        __ num __ mem:
            r.. mem[num]
        __ start __ end:
            mem[num] = nums[start]
            r.. mem[num]
        res1 = nums[start]-helper(nums, start+1, end)
        res2 = nums[end]-helper(nums, start, end-1)
        result = m..(res1, res2)
        mem[num] = result
        r.. result
    
    ___ test
        testCases = [
            [1, 5, 2],
            [1, 5, 233, 7],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = PredictTheWinner_DnC(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
