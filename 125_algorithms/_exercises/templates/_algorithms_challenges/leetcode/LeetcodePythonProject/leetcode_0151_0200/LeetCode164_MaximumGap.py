'''
Created on Feb 12, 2017

@author: MT
'''
class Solution(object
    ___ maximumGap(self, nums
        """
        :type nums: List[int]
        :rtype: int
        """
        ______ ma__
        __ not nums or le.(nums) < 2:
            r_ 0
        minVal = min(nums)
        maxVal = max(nums)
        n = le.(nums)
        gap = ma__.ceil(float(maxVal-minVal)/(n-1))
        bucketsMin = [float('inf')]*(n-1)
        bucketsMax = [float('-inf')]*(n-1)
        ___ num in nums:
            __ num __ minVal or num __ maxVal:
                continue
            idx = int((num-minVal)//gap)
            bucketsMin[idx] = min(bucketsMin[idx], num)
            bucketsMax[idx] = max(bucketsMax[idx], num)
        maxGap = float('-inf')
        prev = minVal
        ___ i in range(n-1
            __ bucketsMin[i] __ float('inf') and bucketsMax[i] __ float('-inf'
                continue
            maxGap = max(maxGap, bucketsMin[i]-prev)
            prev = bucketsMax[i]
        maxGap = max(maxGap, maxVal-prev)
        r_ maxGap
    
    ___ test(self
        testCases = [
            [1, 1000],
        ]
        ___ nums in testCases:
            print('nums: %s' % (nums))
            result = self.maximumGap(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()