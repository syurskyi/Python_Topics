c_ Solution o..
    ___ numberToWords  num
        # https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        ___ words(n
            __ n < 20:
                r_ to19[n - 1:n]
            __ n < 100:
                r_ [tens[n / 10 - 2]] + words(n % 10)
            __ n < 1000:
                r_ [to19[n / 100 - 1]] + ['Hundred'] + words(n % 100)
            ___ p, w __ enumerate(('Thousand', 'Million', 'Billion'), 1
                __ n < 1000 ** (p + 1
                    r_ words(n / 1000 ** p) + [w] + words(n % 1000 ** p)
        r_ ' '.join(words(num)) or 'Zero'
