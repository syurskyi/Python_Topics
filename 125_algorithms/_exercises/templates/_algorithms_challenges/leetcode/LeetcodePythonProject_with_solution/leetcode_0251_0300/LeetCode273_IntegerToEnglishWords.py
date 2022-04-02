'''
Created on Mar 5, 2017

@author: MT
'''
c_ Solution(o..
    ___ numberToWords_own  num
        """
        :type num: int
        :rtype: str
        """
        res = helper(num)
        r.. res __ res ____ 'Zero'
    
    ___ helper  num
        res = ''
        __ num __ 0:
            r.. res
        tokens20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.s.. 
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.s.. 
        __ 0 < num < 20:
            r.. tokens20[num-1]
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
            res += ' ' + helper(remaining)
        ____ num < 1000000:
            first = num/1000
            res += ' ' + helper(first) + ' Thousand'
            remaining = num - first*1000
            res += ' ' + helper(remaining)
        ____ num < 1000000000:
            first = num/1000000
            res += ' ' + helper(first) + ' Million'
            remaining = num - first*1000000
            res += ' ' + helper(remaining)
        ____:
            first = num/1000000000
            res += ' ' + helper(first) + ' Billion'
            remaining = num - first*1000000000
            res += ' ' + helper(remaining)
        r.. res.s..
    
    ___ numberToWords  num
        token20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.s.. 
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.s.. 
        
        ___ words(n
            __ n < 20:
                r.. token20[n-1:n]
            __ n < 100:
                r.. [tens[n/10-2]] + words(n%10)
            __ n < 1000:
                r.. [token20[n/100-1]] +  'Hundred'  + words(n%100)
            ___ p, w __ e..(('Thousand', 'Million', 'Billion'), 1
                __ n < 1000**(p+1
                    r.. words(n/1000**p) + [w] + words(n%1000**p)
        r.. ' '.j..((words(num))) o. 'Zero'