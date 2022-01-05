'''
Created on Oct 30, 2017

@author: MT
'''
c_ Solution(object):
    ___ smallestDistancePair  nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = l..(nums)
        nums.s..()
        low = float('inf')
        ___ i __ r..(n-1):
            low = m..(low, nums[i+1]-nums[i])
        high = nums[-1]-nums[0]
        w.... low < high:
            mid = (low+high)//2
            __ countPair(nums, mid) < k:
                low = mid+1
            ____:
                high = mid
        r.. low
    
    ___ countPair  nums, mid):
        n = l..(nums)
        res = 0
        ___ i __ r..(n):
            res += upperBound(nums, i, n-1, nums[i]+mid)-i-1
        r.. res
    
    ___ upperBound  nums, low, high, key):
        __ nums[high] <= key:
            r.. high+1
        w.... low < high:
            mid = (low+high)//2
            __ key >= nums[mid]:
                low = mid+1
            ____:
                high = mid
        r.. low
    
    ___ countPairs_slow  nums, mid):
        n = l..(nums)
        res = 0
        ___ i __ r..(n):
            j = i
            w.... j < n a.. nums[j]-nums[i] <= mid:
                j += 1
            res += j-i-1
        r.. res
    
    ___ test
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
        ___ nums, k __ testCases:
            print('nums: %s' % nums)
            print('k: %s' % k)
            result = smallestDistancePair(nums, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
