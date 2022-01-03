'''
Created on Feb 22, 2017

@author: MT
'''

c_ Solution(object):
    ___ summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result    # list
        __ n.. nums: r.. result
        i = 0
        w.... i < l..(nums):
            start = nums[i]
            w.... i+1 < l..(nums) a.. nums[i+1] __ nums[i]+1:
                i+=1
            end = nums[i]
            __ end __ start:
                result.a..('%s' % (start))
            ____:
                result.a..('%s->%s' % (start, end))
            i += 1
        r.. result