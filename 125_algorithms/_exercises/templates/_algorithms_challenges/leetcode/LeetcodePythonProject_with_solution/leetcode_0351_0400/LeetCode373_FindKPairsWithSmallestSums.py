'''
Created on Mar 29, 2017

@author: MT
'''

c_ Solution(o..
    ___ kSmallestPairs  nums1, nums2, k
        _______ heapq
        heap    # list
        ___ num1 __ nums1:
            ___ num2 __ nums2:
                heapq.heappush(heap, (num1+num2, num1, num2
        result    # list
        ___ _ __ r..(k
            __ n.. heap:
                _____
            _, num1, num2 heapq.heappop(heap)
            result.a..((num1, num2
        r.. result
    
    ___ test
        testCases [
            (
                [1, 7, 11],
                [2, 4, 6],
                3
            ),
            (
                [1, 1, 2],
                [1, 2, 3],
                2,
            ),
            (
                [1, 2],
                [3],
                3,
            ),
        ]
        ___ nums1, nums2, k __ testCases:
            print('nums1: %s' % nums1)
            print('nums2: %s' % nums2)
            print('k: %s' % k)
            result kSmallestPairs(nums1, nums2, k)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
