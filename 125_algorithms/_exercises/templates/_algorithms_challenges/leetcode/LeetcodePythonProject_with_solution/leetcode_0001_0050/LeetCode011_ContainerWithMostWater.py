'''
Created on Jan 9, 2017

@author: MT
'''

c_ Solution(object):
    ___ maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        __ n.. height: r.. 0
        i, j = 0, l..(height)-1
        area = 0
        w.... i < j:
            area = max(area, m..(height[i], height[j])*(j-i))
            __ height[i] > height[j]:
                j -= 1
            ____:
                i += 1
        r.. area

    ___ test
        testCases = [
            [1, 3, 9, 2],
        ]
        ___ height __ testCases:
            print('height: %s' % (height))
            result = maxArea(height)
            print('result: %s' % (result))
            print('-='*15 + '-')

__ __name__ __ '__main__':
    Solution().test()