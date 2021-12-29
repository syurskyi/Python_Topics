'''
Created on Oct 30, 2017

@author: MT
'''
class Solution(object):
    ___ smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        low = float('inf')
        for i in range(n-1):
            low = min(low, nums[i+1]-nums[i])
        high = nums[-1]-nums[0]
        while low < high:
            mid = (low+high)//2
            __ self.countPair(nums, mid) < k:
                low = mid+1
            else:
                high = mid
        return low
    
    ___ countPair(self, nums, mid):
        n = len(nums)
        res = 0
        for i in range(n):
            res += self.upperBound(nums, i, n-1, nums[i]+mid)-i-1
        return res
    
    ___ upperBound(self, nums, low, high, key):
        __ nums[high] <= key:
            return high+1
        while low < high:
            mid = (low+high)//2
            __ key >= nums[mid]:
                low = mid+1
            else:
                high = mid
        return low
    
    ___ countPairs_slow(self, nums, mid):
        n = len(nums)
        res = 0
        for i in range(n):
            j = i
            while j < n and nums[j]-nums[i] <= mid:
                j += 1
            res += j-i-1
        return res
    
    ___ test(self):
        testCases = [
            [
                [1, 3, 1],
                1,
            ],
            [
                [1, 6, 1],
                3,
            ],
        ]
        for nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.smallestDistancePair(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
