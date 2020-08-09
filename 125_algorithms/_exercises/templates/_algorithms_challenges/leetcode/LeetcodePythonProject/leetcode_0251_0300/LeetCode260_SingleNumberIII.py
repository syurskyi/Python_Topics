'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object
    ___ singleNumber(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        diff = diff&(-diff)
        res = [0, 0]
        for num in nums:
            __ num & diff __ 0:
                res[0] ^= num
            ____
                res[1] ^= num
        r_ res
    
    ___ singleNumber_orig(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        __ not nums or le.(nums) < 2:
            r_ []
        xor = 0
        for num in nums:
            xor ^= num
        group0, group1 = 0, 0
        lastBit = xor-(xor&(xor-1))
        for num in nums:
            __ lastBit & num __ 0:
                group0 ^= num
            ____
                group1 ^= num
        result = [group0, group1]
        r_ result
    
    ___ test(self
        testCases = [
            [1, 2, 1, 3, 2, 5],
        ]
        for nums in testCases:
            print('nums: %s' % (nums))
            result = self.singleNumber(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
    
    ______ random
    for num in range(30
        num = random.randint(0, num)
        print('num:  %08s' % bin(num & 0b11111111))
        print('-num: %8s' % bin(-num & 0b11111111))
        diff = num&(-num)
        print('diff: %8s' % bin(diff & 0b11111111))
        print('-='*30+'-')
