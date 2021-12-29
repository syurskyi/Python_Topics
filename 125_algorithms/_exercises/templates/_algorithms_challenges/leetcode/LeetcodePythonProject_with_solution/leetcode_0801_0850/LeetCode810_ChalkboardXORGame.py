'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object):
    ___ xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ____ functools _______ reduce
        ____ operator _______ xor
        r.. l..(nums)%2__0 o. reduce(xor,nums)__0
    
    ___ xorGame_own_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        r.. self.helper(nums, mem)
    
    ___ helper(self, nums, mem):
        s = s..(nums)
        __ s __ mem:
            r.. mem[s]
        __ self.calc(nums) __ 0:
            mem[s] = True
            r.. True
        flag = False
        ___ i __ r..(l..(nums)):
            __ n.. self.helper(nums[:i]+nums[i+1:], mem):
                flag = True
                break
        mem[s] = flag
        r.. flag
    
    ___ calc(self, nums):
        res = 0
        ___ num __ nums:
            res ^= num
        r.. res
    
    ___ test(self):
        testCases = [
#             [1, 1, 2],
            [1, 1, 2, 3], # True
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = self.xorGame(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
