'''
Created on Oct 1, 2017

@author: MT
'''
c_ Solution(o..):
    ___ findLongestChain  pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        res = 1
        pairs.s..(key=l.... x: (x[1], x[0]))
        maxLen = pairs[0][1]
        ___ i __ r..(1, l..(pairs)):
            pair = pairs[i]
            __ pair[0] > maxLen:
                maxLen = pairs[i][1]
                res += 1
        r.. res
    
    ___ test
        testCases = [
            [[1, 2], [2, 3], [3, 4]],
            [[1, 10], [2, 3], [4, 5], [6, 7]],
        ]
        ___ pairs __ testCases:
            print('pairs: %s' % pairs)
            result = findLongestChain(pairs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
