'''
Created on May 10, 2017

@author: MT
'''

class Solution(object):
    ___ nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res    # list
        ___ k, num0 __ enumerate(findNums):
            ind = nums.index(num0)
            ___ i __ r..(ind, l..(nums)):
                __ nums[i] > num0:
                    res.a..(nums[i])
                    break
            __ l..(res) __ k:
                res.a..(-1)
        r.. res
    
    ___ test(self):
        testCases = [
            (
                [4, 1, 2],
                [1, 3, 4, 2],
            ),
        ]
        ___ findNums, nums __ testCases:
            result = self.nextGreaterElement(findNums, nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
