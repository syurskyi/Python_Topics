'''
Created on Jan 31, 2018

@author: tongq
'''
class Solution(object):
    ___ fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashmap = {}
        ___ a __ A:
            ___ b __ B:
                hashmap[a+b] = hashmap.get(a+b, 0)+1
        res = 0
        ___ c __ C:
            ___ d __ D:
                res += hashmap.get(-c-d, 0)
        r.. res
    
    ___ test(self):
        testCases = [
            [
                [ 1, 2],
                [-2,-1],
                [-1, 2],
                [ 0, 2],
            ],
        ]
        ___ nums1, nums2, nums3, nums4 __ testCases:
            result = self.fourSumCount(nums1, nums2, nums3, nums4)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
