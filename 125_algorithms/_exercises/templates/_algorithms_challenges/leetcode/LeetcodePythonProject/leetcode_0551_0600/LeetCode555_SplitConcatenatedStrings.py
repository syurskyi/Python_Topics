'''
Created on Aug 24, 2017

@author: MT
'''

class Solution(object
    ___ splitLoopedString(self, strs
        """
        :type strs: List[str]
        :rtype: str
        """
        res = None
        arr = [ma.(s, s[::-1]) ___ s __ strs]
        ___ i, s __ enumerate(arr
            ___ start __ (s, s[::-1]
                ___ j __ range(le.(start)+1
                    __ not res:
                        res = start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j]
                    ____
                        res = ma.(res, start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j])
        r_ res
    
    ___ test(self
        testCases = [
            ['abc', 'xyz'],
        ]
        ___ strs __ testCases:
            print('strs: %s' % strs)
            result = self.splitLoopedString(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
