'''
Created on Jan 9, 2017

@author: MT
'''

class Solution(object):
    ___ maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        __ not height: return 0
        i, j = 0, len(height)-1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j])*(j-i))
            __ height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area

    ___ test(self):
        testCases = [
            [1, 3, 9, 2],
        ]
        for height in testCases:
            print('height: %s' % (height))
            result = self.maxArea(height)
            print('result: %s' % (result))
            print('-='*15 + '-')

__ __name__ == '__main__':
    Solution().test()