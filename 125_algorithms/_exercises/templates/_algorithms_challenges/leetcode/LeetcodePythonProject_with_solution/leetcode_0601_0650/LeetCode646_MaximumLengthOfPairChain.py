'''
Created on Oct 1, 2017

@author: MT
'''
class Solution(object):
    ___ findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        res = 1
        pairs.sort(key=l.... x: (x[1], x[0]))
        maxLen = pairs[0][1]
        ___ i __ r..(1, l..(pairs)):
            pair = pairs[i]
            __ pair[0] > maxLen:
                maxLen = pairs[i][1]
                res += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [[1, 2], [2, 3], [3, 4]],
            [[1, 10], [2, 3], [4, 5], [6, 7]],
        ]
        ___ pairs __ testCases:
            print('pairs: %s' % pairs)
            result = self.findLongestChain(pairs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
