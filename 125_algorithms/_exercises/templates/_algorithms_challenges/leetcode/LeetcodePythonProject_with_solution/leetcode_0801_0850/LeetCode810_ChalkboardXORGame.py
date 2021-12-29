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
        from functools import reduce
        from operator import xor
        return len(nums)%2==0 or reduce(xor,nums)==0
    
    ___ xorGame_own_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        return self.helper(nums, mem)
    
    ___ helper(self, nums, mem):
        s = str(nums)
        __ s in mem:
            return mem[s]
        __ self.calc(nums) == 0:
            mem[s] = True
            return True
        flag = False
        for i in range(len(nums)):
            __ not self.helper(nums[:i]+nums[i+1:], mem):
                flag = True
                break
        mem[s] = flag
        return flag
    
    ___ calc(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
    
    ___ test(self):
        testCases = [
#             [1, 1, 2],
            [1, 1, 2, 3], # True
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.xorGame(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
