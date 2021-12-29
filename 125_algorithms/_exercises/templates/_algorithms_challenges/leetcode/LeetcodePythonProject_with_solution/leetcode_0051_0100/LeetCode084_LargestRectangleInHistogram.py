'''
Created on Jan 25, 2017

@author: MT
'''

class Solution(object):
    ___ largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        __ not heights:
            return 0
        area = heights[0]
        i = 0
        while i < len(heights):
            __ not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                h = heights[stack.pop()]
                w = i __ not stack else (i-stack[-1]-1)
                area = max(w*h, area)
        while stack:
            h = heights[stack.pop()]
            w = i __ not stack else (i-stack[-1]-1)
            area = max(area, w*h)
        return area
    
    ___ test(self):
        testCases = [
#             [2,1,5,6,2,3],
            [10, 11, 12, 15],
        ]
        for heights in testCases:
            print('heights: %s' % (heights))
            result = self.largestRectangleArea(heights)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()