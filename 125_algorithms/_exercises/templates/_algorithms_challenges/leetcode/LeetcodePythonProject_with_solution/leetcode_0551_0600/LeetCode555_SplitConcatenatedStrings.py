'''
Created on Aug 24, 2017

@author: MT
'''

class Solution(object):
    ___ splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = N..
        arr = [max(s, s[::-1]) ___ s __ strs]
        ___ i, s __ enumerate(arr):
            ___ start __ (s, s[::-1]):
                ___ j __ r..(l..(start)+1):
                    __ n.. res:
                        res = start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j]
                    ____:
                        res = max(res, start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j])
        r.. res
    
    ___ test(self):
        testCases = [
            ['abc', 'xyz'],
        ]
        ___ strs __ testCases:
            print('strs: %s' % strs)
            result = self.splitLoopedString(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
