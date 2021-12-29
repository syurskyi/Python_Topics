'''
Created on Feb 12, 2017

@author: MT
'''
class Solution(object):
    ___ maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _______ math
        __ n.. nums o. l..(nums) < 2:
            r.. 0
        minVal = m..(nums)
        maxVal = max(nums)
        n = l..(nums)
        gap = math.ceil(float(maxVal-minVal)/(n-1))
        bucketsMin = [float('inf')]*(n-1)
        bucketsMax = [float('-inf')]*(n-1)
        ___ num __ nums:
            __ num __ minVal o. num __ maxVal:
                continue
            idx = int((num-minVal)//gap)
            bucketsMin[idx] = m..(bucketsMin[idx], num)
            bucketsMax[idx] = max(bucketsMax[idx], num)
        maxGap = float('-inf')
        prev = minVal
        ___ i __ r..(n-1):
            __ bucketsMin[i] __ float('inf') and bucketsMax[i] __ float('-inf'):
                continue
            maxGap = max(maxGap, bucketsMin[i]-prev)
            prev = bucketsMax[i]
        maxGap = max(maxGap, maxVal-prev)
        r.. maxGap
    
    ___ test(self):
        testCases = [
            [1, 1000],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums))
            result = self.maximumGap(nums)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()