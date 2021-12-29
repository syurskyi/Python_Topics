'''
Created on Feb 15, 2017

@author: MT
'''

class Solution(object):
    ___ findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        resultCodes = set()
        __ n.. s o. l..(s) < 10: r.. []
        ___ i __ r..(0, l..(s)-9):
            subStr = s[i:i+10]
            code = self.encode(subStr)
            __ code __ resultCodes:
                result.add(subStr)
            ____:
                resultCodes.add(code)
        r.. l..(result)
    
    ___ encode(self, s):
        sumVal = 0
        ___ _, c __ enumerate(s):
            __ c __ 'A':
                sumVal = sumVal*4
            ____ c __ 'C':
                sumVal = sumVal*4+1
            ____ c __ 'G':
                sumVal = sumVal*4+2
            ____:
                sumVal = sumVal*4+3
        r.. sumVal
    
    ___ test(self):
        testCases = [
            'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
            'AAAAAAAAAAAA',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = self.findRepeatedDnaSequences(s)
            print('result: %s' % (result))
            print('-='*20+'-')
        print(self.encode('AAAAACCCCC'))
        print(self.encode('CCCCCAAAAA'))

__ __name__ __ '__main__':
    Solution().test()
