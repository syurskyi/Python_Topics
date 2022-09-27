c_ Solution o..
    ___ myAtoi  s..):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = l.. s..)
        w.. pos < ls and s..[pos] __ ' ':
            pos += 1
        __ pos < ls and s..[pos] __ '-':
            sign = -1
            pos += 1
        ____ pos < ls and s..[pos] __ '+':
            pos += 1
        w.. pos < ls and o.. s..[pos]) >= o.. '0') and o.. s..[pos]) <= o.. '9'):
            num = o.. s..[pos]) - o.. '0')
            __ result > max_int / 10 or ( result __ max_int / 10 and num >= 8):
                __ sign __ -1:
                    r_ min_int
                r_ max_int
            result = result * 10 + num
            pos += 1
        r_ sign * result

    # def myAtoi(self, s):
    #     #https://leetcode.com/discuss/83626/line-python-solution-eafp-instead-lbyl-easier-logic-beats-24%25
    #     try:
    #         s = s.lstrip() + '$' # remove leading spaces and append an end mark
    #         for i, ch in enumerate(s):
    #             if not (ch in '+-' or '0' <= ch <= '9'):
    #                 result = int(s[:i])
    #                 return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
    #     except:
    #         return 0


__ ____ __ ____
    # begin
    s  ?
    print s.myAtoi("+-2")