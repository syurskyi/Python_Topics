'''
Created on Oct 19, 2017

@author: MT
'''
c_ Solution(object):
    ___ judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap    # dict
        r.. helper(nums, hashmap)
    
    ___ helper(self, nums, hashmap):
        __ l..(nums) __ 1:
            r.. abs(nums[0]-24) <= 0.0001
        nums = s..(nums)
        __ ''.j..(s..(nums) + ',') __ hashmap:
            r.. F..
        ___ i __ r..(l..(nums)-1):
            ___ j __ r..(i+1, l..(nums)):
                a = nums[i]
                b = nums[j]
                nums1 = nums[:i]+nums[i+1:j]+nums[j+1:]
                __  helper(nums1 + [a+b], hashmap) o.\
                    helper(nums1 + [a*b], hashmap) o.\
                    helper(nums1 + [b-a], hashmap) o.\
                    helper(nums1 + [a-b], hashmap) o.\
                    (a != 0 a.. helper(nums1 + [float(b)/a], hashmap)) o.\
                    (b != 0 a.. helper(nums1 + [float(a)/b], hashmap)):
                    r.. T..
        hashmap[''.j..(s..(nums)+',')] = F..
        r.. F..
    
    ___ test
        testCases = [
            [4, 1, 8, 7],
            [1, 2, 1, 2],
            [1, 5, 9, 1],
            [1, 8, 2, 5],
            [8, 1, 6, 6],
            [3, 3, 8, 8],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result = judgePoint24(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
