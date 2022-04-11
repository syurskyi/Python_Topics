'''
Created on Feb 19, 2017

@author: MT
'''

c_ Solution(o..
    ___ minSubArrayLen  s, nums
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        start, end 0, 0
        minLen l..(nums) + 1
        sumVal 0
        w.... start <_ end a.. end < l..(nums
            sumVal += nums[end]
            __ sumVal >_ s:
                w.... start <_ end a.. sumVal >_ s:
                    sumVal -_ nums[start]
                    minLen m..(minLen, end-start+1)
                    start+=1
            end+=1
        __ minLen > l..(nums
            r.. 0
        ____
            r.. minLen
    
    ___ minSubArrayLenBS  s, nums
        sums [0]*(l..(nums)+1)
        ___ i __ r..(1, l..(sums:
            sums[i] sums[i-1] + nums[i-1]
        minLen l..(nums)+1
        ___ i __ r..(l..(sums:
            end binarySearch(i+1, l..(sums)-1, sums[i]+s, sums)
            __ end __ l..(sums
                _____
            minLen m..(minLen, end-i)
        r.. minLen __ minLen <_ l..(nums) ____ 0
    
    ___ binarySearch  low, high, key, sums
        w.... low <_ high:
            mid i..((low+high)/2)
            __ sums[mid] >_ key:
                high mid-1
            ____
                low mid+1
        r.. low
    
    ___ test
        testCases [
            (7, [2, 3, 1, 2, 4, 3]),
            (4, [1, 4, 4]),
            (11, [1, 2, 3, 4, 5]),
        ]
        ___ s, nums __ testCases:
            print('nums: %s' % (nums
            print('s: %s' % (s
            result minSubArrayLen(s, nums)
            print('result: %s' % (result
            resultBS minSubArrayLenBS(s, nums)
            print('resultBS: %s' % (resultBS
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()