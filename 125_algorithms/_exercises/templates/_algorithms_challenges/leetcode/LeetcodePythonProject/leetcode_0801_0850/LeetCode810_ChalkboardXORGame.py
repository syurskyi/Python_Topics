'''
Created on Apr 25, 2018

@author: tongq
'''
class Solution(object
    ___ xorGame(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        from functools ______ reduce
        from operator ______ xor
        r_ le.(nums)%2__0 or reduce(xor,nums)__0
    
    ___ xorGame_own_TLE(self, nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        r_ self.helper(nums, mem)
    
    ___ helper(self, nums, mem
        s = str(nums)
        __ s in mem:
            r_ mem[s]
        __ self.calc(nums) __ 0:
            mem[s] = True
            r_ True
        flag = False
        ___ i in range(le.(nums)):
            __ not self.helper(nums[:i]+nums[i+1:], mem
                flag = True
                break
        mem[s] = flag
        r_ flag
    
    ___ calc(self, nums
        res = 0
        ___ num in nums:
            res ^= num
        r_ res
    
    ___ test(self
        testCases = [
#             [1, 1, 2],
            [1, 1, 2, 3], # True
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.xorGame(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
