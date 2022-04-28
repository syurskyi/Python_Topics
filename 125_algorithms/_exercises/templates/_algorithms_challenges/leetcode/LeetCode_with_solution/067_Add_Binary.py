c_ Solution o..
    # def addBinary(self, a, b):
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #     """
    #     res = ''
    #     lsa, lsb = len(a), len(b)
    #     pos = -1
    #     plus = 0
    #     while (lsa + pos) >= 0 and (lsb + pos) >= 0:
    #         curr = int(a[pos]) + int(b[pos]) + plus
    #         if curr >= 2:
    #             plus = 1
    #             curr %= 2
    #         else:
    #             plus = 0
    #         res = str(curr) + res
    #         pos -= 1
    #     if lsa + pos >= 0:
    #         while (lsa + pos) >= 0:
    #             curr = int(a[pos]) + plus
    #             if curr >= 2:
    #                 plus = 1
    #                 curr %= 2
    #             else:
    #                 plus = 0
    #             res = str(curr) + res
    #             pos -= 1
    #     if lsb + pos >= 0:
    #         while (lsb + pos) >= 0:
    #             curr = int(b[pos]) + plus
    #             if curr >= 2:
    #                 plus = 1
    #                 curr %= 2
    #             else:
    #                 plus = 0
    #             res = str(curr) + res
    #             pos -= 1
    #     if plus == 1:
    #         res = '1' + res
    #     return res

    ___ addBinary  a, b):
        res = ''
        lsa, lsb = l.. a), l.. b)
        pos, plus, curr = -1, 0, 0
        # plus a[pos], b[pos] and curr % 2
        w.. (lsa + pos) >= 0 or (lsb + pos) >= 0:
            __ (lsa + pos) >= 0:
                curr += int(a[pos])
            __ (lsb + pos) >= 0:
                curr += int(b[pos])
            res = str(curr % 2) + res
            curr //= 2
            pos -= 1
        __ curr __ 1:
            res = '1' + res
        r_ res
