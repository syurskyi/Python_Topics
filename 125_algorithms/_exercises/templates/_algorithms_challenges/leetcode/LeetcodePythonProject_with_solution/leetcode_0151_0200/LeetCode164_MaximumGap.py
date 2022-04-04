'''
Created on Feb 12, 2017

@author: MT
'''
c_ Solution(o..
    ___ maximumGap  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        _______ m__
        __ n.. nums o. l..(nums) < 2:
            r.. 0
        minVal = m..(nums)
        maxVal = m..(nums)
        n = l..(nums)
        gap = m__.c.. f__(maxVal-minVal)/(n-1
        bucketsMin = [f__('inf')]*(n-1)
        bucketsMax = [f__('-inf')]*(n-1)
        ___ num __ nums:
            __ num __ minVal o. num __ maxVal:
                _____
            idx = i..((num-minVal)//gap)
            bucketsMin[idx] = m..(bucketsMin[idx], num)
            bucketsMax[idx] = m..(bucketsMax[idx], num)
        maxGap = f__('-inf')
        prev = minVal
        ___ i __ r..(n-1
            __ bucketsMin[i] __ f__('inf') a.. bucketsMax[i] __ f__('-inf'
                _____
            maxGap = m..(maxGap, bucketsMin[i]-prev)
            prev = bucketsMax[i]
        maxGap = m..(maxGap, maxVal-prev)
        r.. maxGap
    
    ___ test
        testCases = [
            [1, 1000],
        ]
        ___ nums __ testCases:
            print('nums: %s' % (nums
            result = maximumGap(nums)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()