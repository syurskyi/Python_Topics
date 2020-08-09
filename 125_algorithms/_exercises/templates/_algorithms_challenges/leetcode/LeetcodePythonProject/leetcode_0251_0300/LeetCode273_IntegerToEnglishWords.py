'''
Created on Mar 5, 2017

@author: MT
'''
class Solution(object
    ___ numberToWords_own(self, num
        """
        :type num: int
        :rtype: str
        """
        res = self.helper(num)
        r_ res __ res else 'Zero'
    
    ___ helper(self, num
        res = ''
        __ num __ 0:
            r_ res
        tokens20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        __ 0 < num < 20:
            r_ tokens20[num-1]
        ____ num < 100:
            first = num/10
            res += ' ' + tens[first-2]
            ind = num-first*10-1
            __ ind >= 0:
                res += ' ' + tokens20[ind]
        ____ num < 1000:
            first = num/100
            res += ' ' + tokens20[first-1] + ' Hundred'
            remaining = num-first*100
            res += ' ' + self.helper(remaining)
        ____ num < 1000000:
            first = num/1000
            res += ' ' + self.helper(first) + ' Thousand'
            remaining = num - first*1000
            res += ' ' + self.helper(remaining)
        ____ num < 1000000000:
            first = num/1000000
            res += ' ' + self.helper(first) + ' Million'
            remaining = num - first*1000000
            res += ' ' + self.helper(remaining)
        ____
            first = num/1000000000
            res += ' ' + self.helper(first) + ' Billion'
            remaining = num - first*1000000000
            res += ' ' + self.helper(remaining)
        r_ res.strip()
    
    ___ numberToWords(self, num
        token20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        ___ words(n
            __ n < 20:
                r_ token20[n-1:n]
            __ n < 100:
                r_ [tens[n/10-2]] + words(n%10)
            __ n < 1000:
                r_ [token20[n/100-1]] + ['Hundred'] + words(n%100)
            ___ p, w in enumerate(('Thousand', 'Million', 'Billion'), 1
                __ n < 1000**(p+1
                    r_ words(n/1000**p) + [w] + words(n%1000**p)
        r_ ' '.join((words(num))) or 'Zero'