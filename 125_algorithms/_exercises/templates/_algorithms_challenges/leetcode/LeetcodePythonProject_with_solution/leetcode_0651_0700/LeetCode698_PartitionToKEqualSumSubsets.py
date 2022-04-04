'''
Created on Oct 26, 2017

@author: MT
'''
c_ Solution(o..
    ___ canPartitionKSubsets  nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sumVal = s..(nums)
        __ sumVal%k != 0:
            r.. F..
        nums.s..(r.._T..
        r.. helper(nums, [0]*k, sumVal//k, 0, k)
    
    ___ helper  nums, elems, target, ind, k
        __ ind __ k:
            r.. T..
        ___ i __ r..(l..(nums:
            __ elems[ind]+nums[i] <_ target:
                elems[ind] += nums[i]
                __ elems[ind] __ target a..\
                    helper(nums[:i]+nums[i+1:], elems, target, ind+1, k
                    r.. T..
                ____ helper(nums[:i]+nums[i+1:], elems, target, ind, k
                    r.. T..
                elems[ind] -= nums[i]
            ____
                _____
        r.. F..
    
    ___ test
        testCases = [
            [
                [4, 3, 2, 3, 5, 2, 1],
                4,
            ],
            [
                [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908],
                4,
            ],
            [
                [4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2],
                13,
            ],
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = canPartitionKSubsets(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
