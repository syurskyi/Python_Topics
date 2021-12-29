'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object):
    ___ getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        _______ heapq
        heights    # list
        ___ b __ buildings:
            heights.a..([b[0], -b[2]])
            heights.a..([b[1], b[2]])
        heights.sort()
        heap = [0]
        res    # list
        prev = 0
        ___ h __ heights:
            __ h[1] < 0:
                heapq.heappush(heap, h[1])
            ____:
                heap.remove(-h[1])
                heapq.heapify(heap)
            curr = -heap[0]
            __ curr != prev:
                res.a..([h[0], curr])
            prev = curr
        r.. res
    
    ___ test(self):
        testCases = [
            [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ],
        ]
        ___ buildings __ testCases:
            print('buildings: %s' % (buildings))
            result = self.getSkyline(buildings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
