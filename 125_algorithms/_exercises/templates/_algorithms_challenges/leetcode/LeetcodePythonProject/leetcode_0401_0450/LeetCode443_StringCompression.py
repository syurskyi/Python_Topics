'''
Created on Nov 15, 2017

@author: MT
'''
class Solution(object
    ___ compress(self, chars
        """
        :type chars: List[str]
        :rtype: int
        """
        res = 0
        i = 0
        j = 0
        n = le.(chars)
        w___ i < n:
            __ i+1 < n and chars[i+1] __ chars[i]:
                chars[j] = chars[i]
                j += 1
                prev = i
                w___ i+1 < n and chars[i+1] __ chars[i]:
                    i += 1
                numStr = str(i-prev+1)
                for c0 in numStr:
                    chars[j] = c0
                    j += 1
                res += 1+le.(numStr)
            ____
                chars[j] = chars[i]
                j += 1
                res += 1
            i += 1
        r_ res
    
    ___ test(self
        testCases = [
            'aabbccc',
            'a',
            'abbbbbbbbbbbbb'
        ]
        for chars in testCases:
            chars = list(chars)
            print('chars: %s' % chars)
            result = self.compress(chars)
            print('result: %s' % result)
            print('chars: %s' % chars)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
