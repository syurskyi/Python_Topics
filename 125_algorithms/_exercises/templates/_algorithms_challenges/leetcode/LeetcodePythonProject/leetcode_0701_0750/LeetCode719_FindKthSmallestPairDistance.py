'''
Created on Oct 30, 2017

@author: MT
'''
class Solution(object
    ___ smallestDistancePair(self, nums, k
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = le.(nums)
        nums.sort()
        low = float('inf')
        ___ i in range(n-1
            low = min(low, nums[i+1]-nums[i])
        high = nums[-1]-nums[0]
        w___ low < high:
            mid = (low+high)//2
            __ self.countPair(nums, mid) < k:
                low = mid+1
            ____
                high = mid
        r_ low
    
    ___ countPair(self, nums, mid
        n = le.(nums)
        res = 0
        ___ i in range(n
            res += self.upperBound(nums, i, n-1, nums[i]+mid)-i-1
        r_ res
    
    ___ upperBound(self, nums, low, high, key
        __ nums[high] <= key:
            r_ high+1
        w___ low < high:
            mid = (low+high)//2
            __ key >= nums[mid]:
                low = mid+1
            ____
                high = mid
        r_ low
    
    ___ countPairs_slow(self, nums, mid
        n = le.(nums)
        res = 0
        ___ i in range(n
            j = i
            w___ j < n and nums[j]-nums[i] <= mid:
                j += 1
            res += j-i-1
        r_ res
    
    ___ test(self
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
        ___ nums, k in testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = self.smallestDistancePair(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
