'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object
    ___ maxSlidingWindow(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        deque = []
        ___ i, num in enumerate(nums
            __ deque and deque[0] __ i-k:
                deque.pop(0)
            w___ deque and nums[deque[-1]] < num:
                deque.p..
            deque.append(i)
            __ i+1>=k:
                res.append(nums[deque[0]])
        r_ res
    
    ___ test(self
        testCases = [
            ([1,3,-1,-3,5,3,6,7], 3),
        ]
        ___ nums, k in testCases:
            print('nums: %s' % (nums))
            result = self.maxSlidingWindow(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
