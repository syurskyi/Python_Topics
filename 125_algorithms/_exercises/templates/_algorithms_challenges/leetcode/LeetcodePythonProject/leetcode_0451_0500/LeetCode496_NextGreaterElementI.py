'''
Created on May 10, 2017

@author: MT
'''

class Solution(object
    ___ nextGreaterElement(self, findNums, nums
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        ___ k, num0 in enumerate(findNums
            ind = nums.index(num0)
            ___ i in range(ind, le.(nums)):
                __ nums[i] > num0:
                    res.append(nums[i])
                    break
            __ le.(res) __ k:
                res.append(-1)
        r_ res
    
    ___ test(self
        testCases = [
            (
                [4, 1, 2],
                [1, 3, 4, 2],
            ),
        ]
        ___ findNums, nums in testCases:
            result = self.nextGreaterElement(findNums, nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
