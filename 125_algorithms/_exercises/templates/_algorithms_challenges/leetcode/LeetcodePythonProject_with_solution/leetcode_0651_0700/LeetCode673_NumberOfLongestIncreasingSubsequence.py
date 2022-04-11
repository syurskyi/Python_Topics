'''
Created on Oct 15, 2017

@author: MT
'''
c_ Solution(o..
    ___ findNumberOfLIS  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums: r.. 0
        n l..(nums)
        res 0
        maxLen 0
        lengths [0]*n
        counts [0]*n
        ___ i __ r..(n
            lengths[i], counts[i] 1, 1
            ___ j __ r..(i
                __ nums[i] > nums[j]:
                    __ lengths[i] __ lengths[j]+1:
                        counts[i] += counts[j]
                    ____ lengths[i] < lengths[j]+1:
                        lengths[i] lengths[j] + 1
                        counts[i] counts[j]
            __ maxLen __ lengths[i]:
                res += counts[i]
            ____ maxLen < lengths[i]:
                maxLen lengths[i]
                res counts[i]
        r.. res
    
    ___ test
        testCases [
            [1, 3, 5, 4, 7],
            [2, 2, 2, 2, 2],
            [1, 2, 4, 3, 5, 4, 7, 2],
        ]
        ___ nums __ testCases:
            print('nums: %s' % nums)
            result findNumberOfLIS(nums)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
