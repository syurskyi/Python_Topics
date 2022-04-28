c_ Solution o..
    # def multiply(self, num1, num2):
    #     """
    #     :type num1: str
    #     :type num2: str
    #     :rtype: str
    #     """
    #     res = ''
    #     curr, pos = 0, 0
    #     if len(num1) > num2:
    #         num1, num2 = num2, num1
    #     ls1, ls2 = len(num1), len(num2)
    #     mid = []
    #     for i in reversed(range(ls1)):
    #         curr = 0
    #         fact = ''
    #         for j in reversed(range(ls2)):
    #             curr = curr + int(num1[i]) * int(num2[j])
    #             fact = str(curr % 10) + fact
    #             curr /= 10
    #         if curr > 0:
    #             fact = str(curr) + fact
    #         if int(fact) == 0:
    #             pass
    #         else:
    #             print fact
    #             mid.append(fact + '0' * pos)
    #         pos += 1
    #     res = self.add_strings(mid)
    #     return res
    #
    #
    # def add_strings(self, s_list):
    #     if len(s_list) == 0:
    #         return '0'
    #     res = ''
    #     curr, pos = 0, 0
    #     max_ls = max([len(t) for t in s_list])
    #     while pos < max_ls:
    #         for s in s_list:
    #             if len(s) <= pos:
    #                 continue
    #             curr += int(s[len(s) - pos - 1])
    #         res = str(curr % 10) + res
    #         curr /= 10
    #         pos += 1
    #     if curr > 0:
    #         res = str(curr) + res
    #     return res

    ___ multiply  num1, num2):
        __ num1 __ '0' or num2 __ '0':
            r_ '0'
        res = ''
        ls1, ls2, = l.. num1), l.. num2)
        ls = ls1 + ls2
        # list stores int
        arr = [0] * ls
        ___ i __ reversed(r.. ls1)):
            ___ j __ reversed(r.. ls2)):
                # store the direct results of multiply two ints
                arr[i + j + 1] += int(num1[i]) * int(num2[j])
        ___ i __ reversed(r.. 1, ls)):
            # digital plus
            arr[i - 1] += arr[i] / 10
            arr[i] %= 10
        pos = 0
        # to string
        __ arr[pos] __ 0:
            pos += 1
        w.. pos < ls:
            res = res + str(arr[pos])
            pos += 1
        r_ res


__ ____ __ ____
    s  ?
    print s.multiply("98", "9")
