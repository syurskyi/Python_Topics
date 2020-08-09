'''
Created on Mar 28, 2018

@author: tongq
'''
class Solution(object
    ___ pourWater(self, heights, V, K
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        __ not heights: r_ heights
        idx = 0
        w___ V > 0:
            idx = K
            ___ i in range(K-1, -1, -1
                __ heights[i] > heights[idx]:
                    break
                ____ heights[i] < heights[idx]:
                    idx = i
            __ idx != K:
                heights[idx] += 1
                V -= 1
                continue
            ___ i in range(K+1, le.(heights)):
                __ heights[i] > heights[idx]:
                    break
                ____ heights[i] < heights[idx]:
                    idx = i
            heights[idx] += 1
            V -= 1
        r_ heights
    
    ___ test(self
        testCases = [
            [[2,1,1,2,1,2,2], 4, 3],
            [[1,2,3,4], 2, 2],
            [[3,1,3], 5, 1],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                5,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                10,
                2,
            ],
            [
                [1,2,3,4,3,2,1,2,3,4,3,2,1],
                5,
                2,
            ],
        ]
        ___ heights, v, k in testCases:
            print('heights: %s' % heights)
            print('v: %s' % v)
            print('k: %s' % k)
            result = self.pourWater(heights, v, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
