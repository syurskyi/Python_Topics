'''
Created on Mar 18, 2017

@author: MT
'''
class Solution(object):
    ___ countRangeSum(self, nums, lower, upper):
        first = [0]
        ___ num __ nums:
            first.a..(first[-1]+num)
        r.. self.mergeSort(0, l..(first), first, lower, upper)
    
    ___ mergeSort(self, l, r, first, lower, upper):
        mid = (l+r)//2
        __ mid __ l:
            r.. 0
        count = self.mergeSort(l, mid, first, lower, upper)+\
            self.mergeSort(mid, r, first, lower, upper)
        i, j = mid, mid
        ___ left __ first[l:mid]:
            while i < r and first[i]-left <  lower: i+=1
            while j < r and first[j]-left <= upper: j+=1
            count += j-i
        first[l:r] = s..(first[l:r])
        r.. count
    
    ___ test(self):
        testCases = [
            (
                [-2,5,-1],
                [-2, 2],
            ),
            (
                [0, -3, -3, 1, 1, 2],
                [3, 5],
            ),
            (
                [2147483647,-2147483648,-1,0],
                [-1,0],
            ),
        ]
        ___ nums, (lower, upper) __ testCases:
            print('nums: %s' % (nums))
            print('lower: %s' % (lower))
            print('upper: %s' % (upper))
            result = self.countRangeSum(nums, lower, upper)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
