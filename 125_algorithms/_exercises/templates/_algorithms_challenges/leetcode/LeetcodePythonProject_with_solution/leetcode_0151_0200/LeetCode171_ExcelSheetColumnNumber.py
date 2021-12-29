'''
Created on Feb 13, 2017

@author: MT
'''

class Solution(object):
    ___ titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result*26
            num = ord(c)-ord('A')+1
            result += num
        return result
    
    ___ test(self):
        testCases = [
            'A',
            'B',
            'Z',
            'AA',
            'AAA',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.titleToNumber(s)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ == '__main__':
    Solution().test()