'''
Created on Aug 24, 2017

@author: MT
'''

c_ Solution(o..
    ___ leastBricks  wall
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hashmap    # dict
        ___ vals __ wall:
            sumVal = 0
            ___ val __ vals:
                sumVal += val
                hashmap[sumVal] = hashmap.g.. sumVal, 0)+1
        minRes = l..(wall)
        ___ val, count __ hashmap.i..:
            __ 1 <_ val < s..(wall[0] # not the start and end
                minRes = m..(minRes, l..(wall)-count)
        r.. minRes
    
    ___ test
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
        ___ wall __ testCases:
            print('wall:')
            print('\n'.j..([s..(row) ___ row __ wall]
            result = leastBricks(wall)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
