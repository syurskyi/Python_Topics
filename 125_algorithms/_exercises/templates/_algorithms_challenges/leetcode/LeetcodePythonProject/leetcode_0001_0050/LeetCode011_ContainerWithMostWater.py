'''
Created on Jan 9, 2017

@author: MT
'''

class Solution(object
    ___ maxArea(self, height
        """
        :type height: List[int]
        :rtype: int
        """
        __ not height: r_ 0
        i, j = 0, le.(height)-1
        area = 0
        w___ i < j:
            area = max(area, min(height[i], height[j])*(j-i))
            __ height[i] > height[j]:
                j -= 1
            ____
                i += 1
        r_ area

    ___ test(self
        testCases = [
            [1, 3, 9, 2],
        ]
        for height in testCases:
            print('height: %s' % (height))
            result = self.maxArea(height)
            print('result: %s' % (result))
            print('-='*15 + '-')

__ __name__ __ '__main__':
    Solution().test()