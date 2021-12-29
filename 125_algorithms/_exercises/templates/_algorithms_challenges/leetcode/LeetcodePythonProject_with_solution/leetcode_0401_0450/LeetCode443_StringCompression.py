'''
Created on Nov 15, 2017

@author: MT
'''
class Solution(object):
    ___ compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = 0
        i = 0
        j = 0
        n = l..(chars)
        w.... i < n:
            __ i+1 < n a.. chars[i+1] __ chars[i]:
                chars[j] = chars[i]
                j += 1
                prev = i
                w.... i+1 < n a.. chars[i+1] __ chars[i]:
                    i += 1
                numStr = s..(i-prev+1)
                ___ c0 __ numStr:
                    chars[j] = c0
                    j += 1
                res += 1+l..(numStr)
            ____:
                chars[j] = chars[i]
                j += 1
                res += 1
            i += 1
        r.. res
    
    ___ test(self):
        testCases = [
            'aabbccc',
            'a',
            'abbbbbbbbbbbbb'
        ]
        ___ chars __ testCases:
            chars = l..(chars)
            print('chars: %s' % chars)
            result = self.compress(chars)
            print('result: %s' % result)
            print('chars: %s' % chars)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
