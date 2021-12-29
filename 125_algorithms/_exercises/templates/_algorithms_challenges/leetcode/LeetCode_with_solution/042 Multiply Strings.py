"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
__author__ = 'Danyang'


class Solution(object):
    ___ multiply(self, num1, num2):
        """
        Google Phone Interview Question, 20 Sep 2013
        Steps:
        * multiply by 1 digit at a time
        * add the temporary results up

        To make the processing easier:
        * order the two numbers
        * reverse the numbers

        Solved around 1 hour

        :param num1: String
        :param num2: String
        :return: String
        """
        result    # list

        # pre processing
        __ l..(num1) > l..(num2):  # order them first
            r.. self.multiply(num2, num1)

        # reverse them first
        num1 = map(int, l..(num1[::-1]))
        num2 = map(int, l..(num2[::-1]))

        # multiply by 1 digit at a time
        ___ d __ num1:
            result.a..(self.multiply_1_digit(d, num2))

        # add the temporary results up
        lst = self.add_list(result)

        # post processing
        lst.reverse()  # reverse back
        result = "".join(map(str, lst)).lstrip("0")
        __ n.. result:
            r.. "0"
        r.. result

    ___ multiply_1_digit(self, digit, num):
        """
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        """
        ret    # list

        carry = 0
        ___ elt __ num:
            mul = elt*digit + carry
            carry = mul/10
            mul %= 10
            ret.a..(mul)

        __ carry != 0:
            ret.a..(carry)

        r.. ret

    ___ add_list(self, lst):
        """
        add lst of string
        :param lst:
        :return:
        """
        sig = 0
        ret = [0]
        ___ ind, val __ enumerate(lst):
            ___ i __ xrange(sig): val.insert(0, 0)  # possible deque
            ret = self.add(ret, val)
            sig += 1
        r.. ret

    ___ add(self, num1, num2):
        """
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        """

        __ l..(num1) > l..(num2):
            r.. self.add(num2, num1)

        ret    # list
        carry = 0
        ___ idx __ xrange(l..(num2)):  # longer one
            try:
                sm = num1[idx] + num2[idx] + carry
            except IndexError:
                sm = num2[idx] + carry

            carry = sm/10
            ret.a..(sm % 10)

        __ carry != 0:
            ret.a..(carry)

        r.. ret


__ __name__ __ "__main__":
    solution = Solution()
    ... [1, 2] __ solution.add([2, 1], [9])
    ... str(123*999) __ solution.multiply("123", "999")
    ... str(0) __ solution.multiply("0", "0")
    ... str(123*456) __ solution.multiply("123", "456")
