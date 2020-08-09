'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object
    ___ addBinary(self, a, b
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        __ not a and not b: r_ ''
        __ not a: r_ b
        __ not b: r_ a
        __ le.(a) < le.(b
            tmp = a
            a = b
            b = tmp
        length1 = le.(a)
        length2 = le.(b)
        result = ''
        i1, i2 = length1-1, length2-1
        carry = False
        w___ i2 >= 0:
            c1 = a[i1]
            c2 = b[i2]
            __ c1 __ '0' and c2 __ '0':
                __ carry:
                    result = '1' + result
                ____
                    result = '0' + result
                carry = False
            ____ c1 __ '1' and c2 __ '1':
                __ carry:
                    result = '1' + result
                ____
                    result = '0' + result
                carry = True
            ____
                __ carry:
                    result = '0' + result
                    carry = True
                ____
                    result = '1' + result
                    carry = False
            i1 -= 1
            i2 -= 1
        __ carry:
            __ i1 __ -1:
                result = '1' + result
            ____
                tmp = self.addBinary(a[:i1+1], '1')
                result = tmp + result
        ____
            result = a[:i1+1]+ result
        r_ result
    
    ___ test(self
        testCases = [
            ('11', '1'),
            ('1', '1'),
            ('1', '110'),
        ]
        ___ a, b in testCases:
            print('a: %s, b: %s' % (a, b))
            result = self.addBinary(a, b)
            print('result: %s' % result)
            print('-='*15 + '-')

__ __name__ __ '__main__':
    Solution().test()