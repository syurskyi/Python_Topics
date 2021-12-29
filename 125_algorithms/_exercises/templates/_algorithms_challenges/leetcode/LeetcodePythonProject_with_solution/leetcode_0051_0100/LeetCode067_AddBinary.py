'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ not a and not b: return ''
        __ not a: return b
        __ not b: return a
        __ len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        length1 = len(a)
        length2 = len(b)
        result = ''
        i1, i2 = length1-1, length2-1
        carry = False
        while i2 >= 0:
            c1 = a[i1]
            c2 = b[i2]
            __ c1 == '0' and c2 == '0':
                __ carry:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = False
            elif c1 == '1' and c2 == '1':
                __ carry:
                    result = '1' + result
                else:
                    result = '0' + result
                carry = True
            else:
                __ carry:
                    result = '0' + result
                    carry = True
                else:
                    result = '1' + result
                    carry = False
            i1 -= 1
            i2 -= 1
        __ carry:
            __ i1 == -1:
                result = '1' + result
            else:
                tmp = self.addBinary(a[:i1+1], '1')
                result = tmp + result
        else:
            result = a[:i1+1]+ result
        return result
    
    ___ test(self):
        testCases = [
            ('11', '1'),
            ('1', '1'),
            ('1', '110'),
        ]
        for a, b in testCases:
            print('a: %s, b: %s' % (a, b))
            result = self.addBinary(a, b)
            print('result: %s' % result)
            print('-='*15 + '-')

__ __name__ == '__main__':
    Solution().test()