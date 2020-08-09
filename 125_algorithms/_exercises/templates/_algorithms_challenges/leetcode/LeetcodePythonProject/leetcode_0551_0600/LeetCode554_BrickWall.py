'''
Created on Aug 24, 2017

@author: MT
'''

class Solution(object
    ___ leastBricks(self, wall
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        ___ vals in wall:
            sumVal = 0
            ___ val in vals:
                sumVal += val
                hashmap[sumVal] = hashmap.get(sumVal, 0)+1
        minRes = le.(wall)
        ___ val, count in hashmap.items(
            __ 1 <= val < su.(wall[0] # not the start and end
                minRes = min(minRes, le.(wall)-count)
        r_ minRes
    
    ___ test(self
        testCases = [
            [
                [1,2,2,1],
                [3,1,2],
                [1,3,2],
                [2,4],
                [3,1,2],
                [1,3,1,1],
            ],
        ]
        ___ wall in testCases:
            print('wall:')
            print('\n'.join([str(row) ___ row in wall]))
            result = self.leastBricks(wall)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
