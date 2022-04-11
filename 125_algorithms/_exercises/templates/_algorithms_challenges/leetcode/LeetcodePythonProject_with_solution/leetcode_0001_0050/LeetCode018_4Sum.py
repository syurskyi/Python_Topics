'''
Created on Nov 7, 2017

@author: MT
'''
c_ Solution(o..
    ___ fourSum  nums, target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.s..()
        n l..(nums)
        res    # list
        ___ i __ r..(n-3
            __ i > 0 a.. nums[i] __ nums[i-1]:
                _____
            ___ j __ r..(i+1, n-2
                __ j > i+1 a.. nums[j] __ nums[j-1]:
                    _____
                k, l j+1, n-1
                w.... k < l:
                    tmp  nums[i]+nums[j]+nums[k]+nums[l]
                    __ tmp __ target:
                        res.a..([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -_ 1
                        w.... k < l a.. nums[k-1] __ nums[k]:
                            k += 1
                        w.... k < l a.. nums[l+1] __ nums[l]:
                            l -_ 1
                    ____ tmp < target:
                        k += 1
                    ____
                        l -_ 1
        r.. res
    
    ___ test
        testCases [
            [
                [1,0,-1,0,-2,2],
                0,
            ],
        ]
        ___ nums, target __ testCases:
            print('nums: %s' % nums)
            result fourSum(nums, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
