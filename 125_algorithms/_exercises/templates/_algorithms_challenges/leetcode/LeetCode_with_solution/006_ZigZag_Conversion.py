c_ Solution o..
    # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #     ls = len(s)
    #     if ls <= 1 or numRows == 1:
    #         return s
    #     temp_s = []
    #     for i in range(numRows):
    #         temp_s.append(['']*(ls / 2))
    #     inter = numRows - 1
    #     col, row = 0, 0
    #     for i, ch in enumerate(s):
    #         flag = True
    #         if (i / inter) % 2 == 1:
    #             # print i
    #             flag = False
    #         if flag:
    #             temp_s[row][col] = ch
    #             row += 1
    #         else:
    #             temp_s[row][col] = ch
    #             col += 1
    #             row -= 1
    #     result = ''
    #     for i in range(numRows):
    #         result += ''.join(temp_s[i])
    #     return result

    ___ convert  s, numRows
        # https://leetcode.com/discuss/90908/easy-python-o-n-solution-94%25-with-explanations
        __ numRows __ 1:
            r_ s
        # calculate period
        p = 2 * (numRows - 1)
        result = [""] * numRows
        ___ i __ xrange(l.. s)):
            floor = i % p
            __ floor >= p//2:
                floor = p - floor
            result[floor] += s[i]
        r_ "".join(result)


__ ____ __ ____
    # begin
    s  ?
    print s.convert("PAYPALISHIRING", 3)


