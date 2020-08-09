'''
Created on Feb 20, 2017

@author: MT
'''
class Solution(object
    ___ getSkyline(self, buildings
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ______ heapq
        heights = []
        ___ b in buildings:
            heights.append([b[0], -b[2]])
            heights.append([b[1], b[2]])
        heights.sort()
        heap = [0]
        res = []
        prev = 0
        ___ h in heights:
            __ h[1] < 0:
                heapq.heappush(heap, h[1])
            ____
                heap.remove(-h[1])
                heapq.heapify(heap)
            curr = -heap[0]
            __ curr != prev:
                res.append([h[0], curr])
            prev = curr
        r_ res
    
    ___ test(self
        testCases = [
            [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ],
        ]
        ___ buildings in testCases:
            print('buildings: %s' % (buildings))
            result = self.getSkyline(buildings)
            print('result: %s' % (result))
            print('-='*20+'-')
    
__ __name__ __ '__main__':
    Solution().test()
