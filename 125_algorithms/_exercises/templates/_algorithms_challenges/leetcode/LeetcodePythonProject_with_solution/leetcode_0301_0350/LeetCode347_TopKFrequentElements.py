'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object):
    ___ topKFrequent(self, nums, k):
        maxCount = 0
        hashmap = {}
        ___ num __ nums:
            hashmap[num] = hashmap.get(num, 0)+1
            maxCount = max(maxCount, hashmap[num])
        dp = [[] ___ _ __ r..(maxCount)]
        ___ num, count __ hashmap.items():
            dp[count-1].a..(num)
        result    # list
        i = maxCount-1
        while k > 0:
            __ i < 0:
                break
            __ n.. dp[i]:
                i-=1
            ____:
                result.a..(dp[i].pop(0))
                k-=1
        r.. result
        
    
    ___ topKFrequentHeap(self, nums, k):
        _______ heapq
        hashmap = {}
        ___ num __ nums:
            hashmap[num] = hashmap.get(num, 0)+1
        heap    # list
        ___ num, count __ hashmap.items():
            heapq.heappush(heap, (-count, num))
        result    # list
        while k > 0:
            result.a..(heapq.heappop(heap)[1])
            k -= 1
        r.. result
    
    ___ test(self):
        testCases = [
#             ([1, 1, 1, 2, 2, 3], 2),
            ([1,1,1,2,2,2,3,3,3], 3),
        ]
        ___ nums, k __ testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.topKFrequent(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
