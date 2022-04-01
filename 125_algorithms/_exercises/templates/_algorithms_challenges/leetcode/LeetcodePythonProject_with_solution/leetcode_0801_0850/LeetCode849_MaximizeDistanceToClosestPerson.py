'''
Created on Jun 10, 2019

@author: tongq
'''
c_ Solution(o..):
    ___ maxDistToClosest  seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = i = 0
        ___ j __ r..(l..(seats)):
            __ seats[j] __ 1:
                __ i __ 0:
                    res = j
                ____:
                    res = m..(res, (j-i+1) >> 1)
                i = j+1
        r.. m..(res, l..(seats)-i)
    
    ___ maxDistToClosest_twoPass  seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # two passes, there is a better solution for one pass
        n = l..(seats)
        left = [0]*(n+1)
        right = [0]*(n+1)
        left[0] = f__('inf')
        ___ i __ r..(n):
            __ seats[i] __ 0:
                left[i+1] = left[i]+1
        right[-1] = f__('inf')
        ___ i __ r..(n-1, -1, -1):
            __ seats[i] __ 0:
                right[i] = right[i+1]+1
        res = f__('-inf')
        ___ i __ r..(n):
            __ left[i+1] != 0 a.. right[i] != 0:
                res = m..(res, m..(left[i+1], right[i]))
        r.. res
    
    ___ test
        testCases = [
            [1,0,0,0,1,0,1],
            [1,0,0,0],
            [0,1],
            [1,0],
        ]
        ___ seats __ testCases:
            result = maxDistToClosest(seats)
            print('result: %s' % result)
            print('-='*30)

__ _____ __ _____
    Solution().test()
