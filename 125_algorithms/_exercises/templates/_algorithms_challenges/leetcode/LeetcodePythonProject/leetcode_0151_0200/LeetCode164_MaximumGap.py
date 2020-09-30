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
        maxVal = ma.(nums)
        n = le.(nums)
        gap = ma__.ceil(float(maxVal-minVal)/(n-1))
        bucketsMin = [float('inf')]*(n-1)
        bucketsMax = [float('-inf')]*(n-1)
        ___ num __ nums:
            __ num __ minVal or num __ maxVal:
                continue
            idx = int((num-minVal)//gap)
            bucketsMin[idx] = min(bucketsMin[idx], num)
            bucketsMax[idx] = ma.(bucketsMax[idx], num)
        maxGap = float('-inf')
        prev = minVal
        ___ i __ range(n-1
            __ bucketsMin[i] __ float('inf') and bucketsMax[i] __ float('-inf'
                continue
            maxGap = ma.(maxGap, bucketsMin[i]-prev)
            prev = bucketsMax[i]
        maxGap = ma.(maxGap, maxVal-prev)
        r_ maxGap
    
    ___ test(self
        testCases = [
            [1, 1000],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.maximumGap(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__  -n __ '__main__':
    Solution().test()