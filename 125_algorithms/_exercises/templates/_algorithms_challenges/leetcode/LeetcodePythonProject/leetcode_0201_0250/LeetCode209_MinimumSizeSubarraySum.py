'''
Created on Feb 19, 2017

@author: MT
'''

class Solution(object
    ___ minSubArrayLen(self, s, nums
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        __ not nums: r_ 0
        start, end = 0, 0
        minLen = le.(nums) + 1
        sumVal = 0
        w___ start <= end and end < le.(nums
            sumVal += nums[end]
            __ sumVal >= s:
                w___ start <= end and sumVal >= s:
                    sumVal -= nums[start]
                    minLen = min(minLen, end-start+1)
                    start+=1
            end+=1
        __ minLen > le.(nums
            r_ 0
        ____
            r_ minLen
    
    ___ minSubArrayLenBS(self, s, nums
        sums = [0]*(le.(nums)+1)
        ___ i in range(1, le.(sums)):
            sums[i] = sums[i-1] + nums[i-1]
        minLen = le.(nums)+1
        ___ i in range(le.(sums)):
            end = self.binarySearch(i+1, le.(sums)-1, sums[i]+s, sums)
            __ end __ le.(sums
                break
            minLen = min(minLen, end-i)
        r_ minLen __ minLen <= le.(nums) else 0
    
    ___ binarySearch(self, low, high, key, sums
        w___ low <= high:
            mid = int((low+high)/2)
            __ sums[mid] >= key:
                high = mid-1
            ____
                low = mid+1
        r_ low
    
    ___ test(self
        testCases = [
            (7, [2, 3, 1, 2, 4, 3]),
            (4, [1, 4, 4]),
            (11, [1, 2, 3, 4, 5]),
        ]
        ___ s, nums in testCases:
            print('nums: %s' % (nums))
            print('s: %s' % (s))
            result = self.minSubArrayLen(s, nums)
            print('result: %s' % (result))
            resultBS = self.minSubArrayLenBS(s, nums)
            print('resultBS: %s' % (resultBS))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()