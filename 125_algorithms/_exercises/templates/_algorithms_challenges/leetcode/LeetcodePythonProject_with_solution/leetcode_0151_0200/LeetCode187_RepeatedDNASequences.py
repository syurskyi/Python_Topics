'''
Created on Feb 15, 2017

@author: MT
'''

c_ Solution(object):
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
            code = encode(subStr)
            __ code __ resultCodes:
                result.add(subStr)
            ____:
                resultCodes.add(code)
        r.. l..(result)
    
    ___ encode(self, s):
        sumVal = 0
        ___ _, c __ e..(s):
            __ c __ 'A':
                sumVal = sumVal*4
            ____ c __ 'C':
                sumVal = sumVal*4+1
            ____ c __ 'G':
                sumVal = sumVal*4+2
            ____:
                sumVal = sumVal*4+3
        r.. sumVal
    
    ___ test
        testCases = [
            'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT',
            'AAAAAAAAAAAA',
        ]
        ___ s __ testCases:
            print('s: %s' % (s))
            result = findRepeatedDnaSequences(s)
            print('result: %s' % (result))
            print('-='*20+'-')
        print(encode('AAAAACCCCC'))
        print(encode('CCCCCAAAAA'))

__ _____ __ _____
    Solution().test()
