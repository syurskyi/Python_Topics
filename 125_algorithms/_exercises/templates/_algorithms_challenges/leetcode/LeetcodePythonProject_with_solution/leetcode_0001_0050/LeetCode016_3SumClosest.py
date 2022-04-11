'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ threeSumClosest  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.s..()
        res = f__('inf')
        n = l..(nums)
        ___ i __ r..(n-2
            j, k = i+1, n-1
            w.... j < k:
                tmp  nums[i]+nums[j]+nums[k]
                diff = a..(tmp-target)
                __ diff < a..(res-target
                    res = tmp
                __ tmp __ target:
                    r.. target
                ____ tmp > target:
                    k -_ 1
                ____
                    j += 1
        r.. res
    
    ___ test
        testCases = [
            [
                [-1, 2, 1, -4],
                1,
            ],
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % nums)
            print('target: %s' % target)
            result = threeSumClosest(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
