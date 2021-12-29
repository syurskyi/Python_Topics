'''
Created on Feb 26, 2017

@author: MT
'''

class Solution(object):
    ___ maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res    # list
        deque    # list
        ___ i, num __ e..(nums):
            __ deque a.. deque[0] __ i-k:
                deque.pop(0)
            w.... deque a.. nums[deque[-1]] < num:
                deque.pop()
            deque.a..(i)
            __ i+1>=k:
                res.a..(nums[deque[0]])
        r.. res
    
    ___ test(self):
        testCases = [
            ([1,3,-1,-3,5,3,6,7], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            result = self.maxSlidingWindow(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
