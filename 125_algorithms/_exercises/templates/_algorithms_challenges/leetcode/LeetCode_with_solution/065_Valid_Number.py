c_ Solution o..
    # def isNumber(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     # remove lead and tail space
    #     s = s.strip()
    #     try:
    #         float(s)
    #         return True
    #     except:
    #         if '.' in s or ' ' in s:
    #             return False
    #         temp = s.split('e')
    #         if len(temp) == 2:
    #             try:
    #                 int(temp[0])
    #                 int(temp[1])
    #             except:
    #                 return False
    #             return True
    #     return False

    ___ isNumber  s):
        s = s.strip()
        ls, pos = l.. s), 0
        __ ls __ 0:
            r_ False
        __ s[pos] __ '+' or s[pos] __ '-':
            pos += 1
        isNumeric = False
        w.. pos < ls and s[pos].isdigit():
            pos += 1
            isNumeric = True
        __ pos < ls and s[pos] __ '.':
            pos += 1
            w.. pos < ls and s[pos].isdigit():
                pos += 1
                isNumeric = True
        ____ pos < ls and s[pos] __ 'e' and isNumeric:
            isNumeric = False
            pos += 1
            __ pos < ls and (s[pos] __ '+' or s[pos] __ '-'):
                pos += 1
            w.. pos < ls and s[pos].isdigit():
                pos += 1
                isNumeric = True
        print pos, ls, isNumeric
        __ pos __ ls and isNumeric:
            r_ True
        r_ False
