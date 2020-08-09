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
        arr = [max(s, s[::-1]) for s in strs]
        for i, s in enumerate(arr
            for start in (s, s[::-1]
                for j in range(le.(start)+1
                    __ not res:
                        res = start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j]
                    ____
                        res = max(res, start[j:] + ''.join(arr[i+1:]+arr[:i]) + start[:j])
        r_ res
    
    ___ test(self
        testCases = [
            ['abc', 'xyz'],
        ]
        for strs in testCases:
            print('strs: %s' % strs)
            result = self.splitLoopedString(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
