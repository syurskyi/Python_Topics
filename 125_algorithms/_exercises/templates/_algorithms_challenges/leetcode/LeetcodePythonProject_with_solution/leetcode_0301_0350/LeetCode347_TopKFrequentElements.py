'''
Created on Mar 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ topKFrequent  nums, k
        maxCount 0
        hashmap    # dict
        ___ num __ nums:
            hashmap[num] hashmap.g.. num, 0)+1
            maxCount m..(maxCount, hashmap[num])
        dp [[] ___ _ __ r..(maxCount)]
        ___ num, count __ hashmap.i..
            dp[count-1].a..(num)
        result    # list
        i maxCount-1
        w.... k > 0
            __ i < 0:
                _____
            __ n.. dp[i]:
                i-_1
            ____
                result.a..(dp[i].p.. 0
                k-_1
        r.. result
        
    
    ___ topKFrequentHeap  nums, k
        _______ h__
        hashmap    # dict
        ___ num __ nums:
            hashmap[num] hashmap.g.. num, 0)+1
        heap    # list
        ___ num, count __ hashmap.i..
            h__.heappush(heap, (-count, num
        result    # list
        w.... k > 0
            result.a..(h__.heappop(heap)[1])
            k -_ 1
        r.. result
    
    ___ test
        testCases [
#             ([1, 1, 1, 2, 2, 3], 2),
            ([1,1,1,2,2,2,3,3,3], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums
            print('k: %s' % (k
            result topKFrequent(nums, k)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
