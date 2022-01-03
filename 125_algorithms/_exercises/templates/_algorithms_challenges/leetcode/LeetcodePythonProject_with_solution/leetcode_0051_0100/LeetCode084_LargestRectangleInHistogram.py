'''
Created on Jan 25, 2017

@author: MT
'''

c_ Solution(object):
    ___ largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack    # list
        __ n.. heights:
            r.. 0
        area = heights[0]
        i = 0
        w.... i < l..(heights):
            __ n.. stack o. heights[i] >= heights[stack[-1]]:
                stack.a..(i)
                i+=1
            ____:
                h = heights[stack.pop()]
                w = i __ n.. stack ____ (i-stack[-1]-1)
                area = max(w*h, area)
        w.... stack:
            h = heights[stack.pop()]
            w = i __ n.. stack ____ (i-stack[-1]-1)
            area = max(area, w*h)
        r.. area
    
    ___ test
        testCases = [
#             [2,1,5,6,2,3],
            [10, 11, 12, 15],
        ]
        ___ heights __ testCases:
            print('heights: %s' % (heights))
            result = largestRectangleArea(heights)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()