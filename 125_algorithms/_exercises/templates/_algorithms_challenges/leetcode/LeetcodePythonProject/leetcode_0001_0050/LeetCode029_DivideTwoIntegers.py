'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object
    ___ divide(self, dividend, divisor
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n
        sign = 1
        __ (dividend > 0 and divisor < 0) or\
            (dividend < 0 and divisor > 0
            sign = -1
        __ dividend < 0: dividend = -dividend
        __ divisor < 0: divisor = -divisor
        __ divisor __ 0: r_ 2**32-1
        __ dividend __ 0 or dividend < divisor:
            r_ 0
        res = self.ldivide(dividend, divisor)
        __ res >= 2**31-1:
            res = 2**31-1 __ sign __ 1 else -2**31
        ____
            res = res __ sign > 0 else -res
        r_ res
        
    ___ ldivide(self, dividend, divisor
        __ dividend < divisor: r_ 0
        sumVal = divisor
        multiple = 1
        w___ sumVal+sumVal <= dividend:
            sumVal += sumVal
            multiple += multiple
        r_ multiple + self.ldivide(dividend-sumVal, divisor)
    
    ___ test(self
        testCases = [
            [1, 1],
            [5, 2],
            [-1, 1],
            [-2147483648, -1],
        ]
        ___ dividend, divisor in testCases:
            print('dividend: %s' % dividend)
            print('divisor: %s' % divisor)
            result = self.divide(dividend, divisor)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
