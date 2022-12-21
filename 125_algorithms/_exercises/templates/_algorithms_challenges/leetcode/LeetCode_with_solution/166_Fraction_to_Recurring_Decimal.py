c_ Solution o..
    ___ fractionToDecimal  numerator, denominator
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        __ numerator __ 0:
            r_ '0'
        fraction = ''
        __ (numerator < 0) ^ (denominator < 0
            fraction += '-'
        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction += s..(dividend / divisor)
        remainder = dividend % divisor
        __ remainder __ 0:
            r_ fraction
        fraction += '.'
        dic  # dict
        w.. remainder != 0:
            __ remainder __ dic:
                fraction = fraction[:dic[remainder]] + '(' + fraction[dic[remainder]:] + ')'
                break
            dic[remainder] = l.. fraction)
            remainder *= 10
            fraction += s..(remainder / divisor)
            remainder %= divisor
        r_ fraction


__ ____ __ ____
    s  ?
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.fractionToDecimal(-50, 8)
