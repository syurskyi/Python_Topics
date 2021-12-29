'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object):
    ___ findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset = set()
        n = len(nums)
        sumVal = n*(n+1)//2
        res = []
        for num in nums:
            __ num not in hashset:
                hashset.add(num)
                sumVal -= num
            else:
                res.append(num)
        res.append(sumVal)
        return res
    
    ___ test(self):
        testCases = [
            [1, 2, 2, 4],
        ]
        for nums in testCases:
            print('nums: %s' % nums)
            result = self.findErrorNums(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
