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
        __ not s or len(s) < 10: return []
        for i in range(0, len(s)-9):
            subStr = s[i:i+10]
            code = self.encode(subStr)
            __ code in resultCodes:
                result.add(subStr)
            else:
                resultCodes.add(code)
        return list(result)
    
    ___ encode(self, s):
        sumVal = 0
        for _, c in enumerate(s):
            __ c == 'A':
                sumVal = sumVal*4
            elif c == 'C':
                sumVal = sumVal*4+1
            elif c == 'G':
                sumVal = sumVal*4+2
            else:
                sumVal = sumVal*4+3
        return sumVal
    
    ___ test(self):
        testCases = [
            'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
            'AAAAAAAAAAAA',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.findRepeatedDnaSequences(s)
            print('result: %s' % (result))
            print('-='*20+'-')
        print(self.encode('AAAAACCCCC'))
        print(self.encode('CCCCCAAAAA'))

__ __name__ == '__main__':
    Solution().test()
