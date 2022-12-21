c_ Solution o..
    # def restoreIpAddresses(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     ls = len(s)
    #     if ls == 0 or ls > 12:
    #         return []
    #     if s == '0000':
    #         return ['0.0.0.0']
    #     return self.getremainIP(s, 0, 4)
    #
    # def getremainIP(self, s, pos, count):
    #     if count == 1:
    #         curr = s[pos:]
    #         if self.isNum(curr):
    #             return [curr]
    #     result = []
    #     for i in range(pos, pos + 3):
    #         if i + 1 < len(s):
    #             prefix = s[pos:i + 1]
    #             if self.isNum(prefix):
    #                 res = self.getremainIP(s, i + 1, count - 1)
    #                 result.extend([prefix + '.' + t for t in res])
    #     return result
    #
    # def isNum(self, prefix):
    #     curr = int(prefix)
    #     if curr > 255:
    #         return False
    #     if len(prefix) == 1:
    #         return True
    #     if prefix[0] == '0':
    #         return False
    #     return True

    ___ restoreIpAddresses  s
        ls = l.. s)
        __ ls __ 0 or ls > 12:
            r_    # list
        res =    # list
        ___ i __ r.. 1, 4
            ___ j __ r.. 1, 4
                ___ k __ r.. 1, 4
                    m = ls - i - j - k
                    __ m > 0 and m <= 3:
                        add1 = s[0:i]
                        add2 = s[i:i + j]
                        add3 = s[i + j:i + j + k]
                        add4 = s[i + j + k:]
                        __ isValid(add1) and isValid(add2) and \
                                        isValid(add3) and isValid(add4
                            res.append(add1 + '.' + add2 + '.' + add3 + '.' + add4)
        r_ res

    ___ isValid  add
        __ l.. add) __ 1:
            r_ T..
        __ add[0] __ '0':
            r_ F..
        __ i..(add) <= 255:
            r_ T..
        r_ F..


__ ____ __ ____
    s  ?
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.restoreIpAddresses('25525511135')

