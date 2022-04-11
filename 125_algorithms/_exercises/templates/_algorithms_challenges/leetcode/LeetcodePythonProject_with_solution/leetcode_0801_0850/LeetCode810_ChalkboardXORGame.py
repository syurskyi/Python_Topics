'''
Created on Apr 25, 2018

@author: tongq
'''
c_ Solution(o..
    ___ xorGame  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        ____ f.. _______ r..
        ____ o.. _______ xor
        r.. l..(nums)%2__0 o. r.. xor,nums)__0
    
    ___ xorGame_own_TLE  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem    # dict
        r.. helper(nums, mem)
    
    ___ helper  nums, mem
        s s..(nums)
        __ s __ mem:
            r.. mem[s]
        __ calc(nums) __ 0:
            mem[s] T..
            r.. T..
        flag F..
        ___ i __ r..(l..(nums:
            __ n.. helper(nums[:i]+nums[i+1:], mem
                flag T..
                _____
        mem[s] flag
        r.. flag
    
    ___ calc  nums
        res 0
        ___ num __ nums:
            res ^= num
        r.. res
    
    ___ test
        testCases [
#             [1, 1, 2],
            [1, 1, 2, 3], # True
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result xorGame(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
