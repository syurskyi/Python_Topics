'''
Created on Feb 14, 2017

@author: MT
'''
#TODO: cannot do this using Python 3 because cmp is not available
c_ Solution:
    # @param {integer[]} nums
    # @return {string}
    ___ largestNumber(self, nums):
        comp = l.... a, b: 1 __ a+b > b+a ____ -1 __ a+b<b+a ____ 0
        nums = l..(map(s.., nums))
        nums.s..(cmp=comp, r.._T..
        r.. ''.j..(nums).lstrip('0')
    
    # @param {integer[]} nums
    # @return {string}
    ___ largestNumber_python2(self, nums):
        #python 2 only
        num = [s..(x) ___ x __ nums]
#         num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        r.. ''.j..(num).lstrip('0') o. '0'
    
    ___ test
        testCases = [
            [3, 30, 34, 5, 9],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = largestNumber(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()