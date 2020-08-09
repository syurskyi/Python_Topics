'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object
    ___ findErrorNums(self, nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashset = set()
        n = le.(nums)
        sumVal = n*(n+1)//2
        res = []
        ___ num in nums:
            __ num not in hashset:
                hashset.add(num)
                sumVal -= num
            ____
                res.append(num)
        res.append(sumVal)
        r_ res
    
    ___ test(self
        testCases = [
            [1, 2, 2, 4],
        ]
        ___ nums in testCases:
            print('nums: %s' % nums)
            result = self.findErrorNums(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
