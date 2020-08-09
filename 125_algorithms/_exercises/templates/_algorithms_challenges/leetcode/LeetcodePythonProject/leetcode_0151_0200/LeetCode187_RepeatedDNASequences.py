'''
Created on Feb 15, 2017

@author: MT
'''

class Solution(object
    ___ findRepeatedDnaSequences(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        resultCodes = set()
        __ not s or le.(s) < 10: r_ []
        ___ i in range(0, le.(s)-9
            subStr = s[i:i+10]
            code = self.encode(subStr)
            __ code in resultCodes:
                result.add(subStr)
            ____
                resultCodes.add(code)
        r_ list(result)
    
    ___ encode(self, s
        sumVal = 0
        ___ _, c in enumerate(s
            __ c __ 'A':
                sumVal = sumVal*4
            ____ c __ 'C':
                sumVal = sumVal*4+1
            ____ c __ 'G':
                sumVal = sumVal*4+2
            ____
                sumVal = sumVal*4+3
        r_ sumVal
    
    ___ test(self
        testCases = [
            'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
            'AAAAAAAAAAAA',
        ]
        ___ s in testCases:
            print('s: %s' % (s))
            result = self.findRepeatedDnaSequences(s)
            print('result: %s' % (result))
            print('-='*20+'-')
        print(self.encode('AAAAACCCCC'))
        print(self.encode('CCCCCAAAAA'))

__ __name__ __ '__main__':
    Solution().test()
