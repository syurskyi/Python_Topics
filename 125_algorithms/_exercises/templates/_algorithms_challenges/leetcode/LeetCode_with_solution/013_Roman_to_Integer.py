c_ Solution:
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     roman = {'I': 1, 'V': 5, 'X': 10,
    #              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     result = 0
    #     last = s[-1]
    #     for t in reversed(s):
    #         if t == 'C' and last in ['D', 'M']:
    #             result -= roman[t]
    #         elif t == 'X' and last in ['L', 'C']:
    #             result -= roman[t]
    #         elif t == 'I' and last in ['V', 'X']:
    #             result -= roman[t]
    #         else:
    #             result += roman[t]
    #         last = t
    #     return result

    ___ romanToInt  s
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        ___ c __ s:
            curr = roman[c]
            total += curr
            # need to subtract
            __ curr > prev:
                total -= 2 * prev
            prev = curr
        r_ total

