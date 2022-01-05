'''
Created on Mar 18, 2017

@author: MT
'''
c_ Solution(object):
    ___ countRangeSum  nums, lower, upper):
        first = [0]
        ___ num __ nums:
            first.a..(first[-1]+num)
        r.. mergeSort(0, l..(first), first, lower, upper)
    
    ___ mergeSort  l, r, first, lower, upper):
        mid = (l+r)//2
        __ mid __ l:
            r.. 0
        count = mergeSort(l, mid, first, lower, upper)+\
            mergeSort(mid, r, first, lower, upper)
        i, j = mid, mid
        ___ left __ first[l:mid]:
            w.... i < r a.. first[i]-left <  lower: i+=1
            w.... j < r a.. first[j]-left <= upper: j+=1
            count += j-i
        first[l:r] = s..(first[l:r])
        r.. count
    
    ___ test
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
            result = countRangeSum(nums, lower, upper)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
