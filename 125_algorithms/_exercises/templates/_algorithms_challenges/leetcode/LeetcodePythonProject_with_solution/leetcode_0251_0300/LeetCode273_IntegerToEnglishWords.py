'''
Created on Mar 5, 2017

@author: MT
'''
class Solution(object):
    ___ numberToWords_own(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = self.helper(num)
        return res __ res else 'Zero'
    
    ___ helper(self, num):
        res = ''
        __ num == 0:
            return res
        tokens20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        __ 0 < num < 20:
            return tokens20[num-1]
        elif num < 100:
            first = num/10
            res += ' ' + tens[first-2]
            ind = num-first*10-1
            __ ind >= 0:
                res += ' ' + tokens20[ind]
        elif num < 1000:
            first = num/100
            res += ' ' + tokens20[first-1] + ' Hundred'
            remaining = num-first*100
            res += ' ' + self.helper(remaining)
        elif num < 1000000:
            first = num/1000
            res += ' ' + self.helper(first) + ' Thousand'
            remaining = num - first*1000
            res += ' ' + self.helper(remaining)
        elif num < 1000000000:
            first = num/1000000
            res += ' ' + self.helper(first) + ' Million'
            remaining = num - first*1000000
            res += ' ' + self.helper(remaining)
        else:
            first = num/1000000000
            res += ' ' + self.helper(first) + ' Billion'
            remaining = num - first*1000000000
            res += ' ' + self.helper(remaining)
        return res.strip()
    
    ___ numberToWords(self, num):
        token20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        ___ words(n):
            __ n < 20:
                return token20[n-1:n]
            __ n < 100:
                return [tens[n/10-2]] + words(n%10)
            __ n < 1000:
                return [token20[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                __ n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        return ' '.join((words(num))) or 'Zero'