c_ Solution o..
    # def plusOne(self, digits):
    #     """
    #     :type digits: List[int]
    #     :rtype: List[int]
    #     """
    #     ls = len(digits)
    #     curr, pos = 1, 0
    #     while pos < ls:
    #         index = ls - pos - 1
    #         curr += digits[index]
    #         digits[index] = curr % 10
    #         curr /= 10
    #         if curr == 0:
    #             # do not need to continue
    #             break
    #         pos += 1
    #     if curr > 0:
    #         digits.insert(0, curr)
    #     return digits

    ___ plusOne  digits):
        ls = l.. digits)
        ___ index __ reversed(r.. ls)):
            __ digits[index] < 9:
                digits[index] += 1
                # do not need to continue
                r_ digits
            ____
                # 10
                digits[index] = 0
        digits.insert(0, 1)
        r_ digits


