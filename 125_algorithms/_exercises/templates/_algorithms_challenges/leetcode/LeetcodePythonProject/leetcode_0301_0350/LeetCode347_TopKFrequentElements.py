'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object
    ___ topKFrequent(self, nums, k
        maxCount = 0
        hashmap = {}
        ___ num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
            maxCount = max(maxCount, hashmap[num])
        dp = [[] ___ _ in range(maxCount)]
        ___ num, count in hashmap.items(
            dp[count-1].append(num)
        result = []
        i = maxCount-1
        w___ k > 0:
            __ i < 0:
                break
            __ not dp[i]:
                i-=1
            ____
                result.append(dp[i].pop(0))
                k-=1
        r_ result
        
    
    ___ topKFrequentHeap(self, nums, k
        ______ heapq
        hashmap = {}
        ___ num in nums:
            hashmap[num] = hashmap.get(num, 0)+1
        heap = []
        ___ num, count in hashmap.items(
            heapq.heappush(heap, (-count, num))
        result = []
        w___ k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        r_ result
    
    ___ test(self
        testCases = [
#             ([1, 1, 1, 2, 2, 3], 2),
            ([1,1,1,2,2,2,3,3,3], 3),
        ]
        ___ nums, k in testCases:
            print('nums: %s' % (nums))
            print('k: %s' % (k))
            result = self.topKFrequent(nums, k)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
