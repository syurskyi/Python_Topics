"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
__author__ = 'Danyang'


class Solution(object
    ___ multiply(self, num1, num2
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
        result = []

        # pre processing
        __ le.(num1) > le.(num2  # order them first
            r_ self.multiply(num2, num1)

        # reverse them first
        num1 = map(int, list(num1[::-1]))
        num2 = map(int, list(num2[::-1]))

        # multiply by 1 digit at a time
        ___ d in num1:
            result.append(self.multiply_1_digit(d, num2))

        # add the temporary results up
        lst = self.add_list(result)

        # post processing
        lst.reverse()  # reverse back
        result = "".join(map(str, lst)).lstrip("0")
        __ not result:
            r_ "0"
        r_ result

    ___ multiply_1_digit(self, digit, num
        """
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        """
        ret = []

        carry = 0
        ___ elt in num:
            mul = elt*digit + carry
            carry = mul/10
            mul %= 10
            ret.append(mul)

        __ carry != 0:
            ret.append(carry)

        r_ ret

    ___ add_list(self, lst
        """
        add lst of string
        :param lst:
        :return:
        """
        sig = 0
        ret = [0]
        ___ ind, val in enumerate(lst
            ___ i in xrange(sig val.insert(0, 0)  # possible deque
            ret = self.add(ret, val)
            sig += 1
        r_ ret

    ___ add(self, num1, num2
        """
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        """

        __ le.(num1) > le.(num2
            r_ self.add(num2, num1)

        ret = []
        carry = 0
        ___ idx in xrange(le.(num2)):  # longer one
            try:
                sm = num1[idx] + num2[idx] + carry
            except IndexError:
                sm = num2[idx] + carry

            carry = sm/10
            ret.append(sm % 10)

        __ carry != 0:
            ret.append(carry)

        r_ ret


__ __name__ __ "__main__":
    solution = Solution()
    assert [1, 2] __ solution.add([2, 1], [9])
    assert str(123*999) __ solution.multiply("123", "999")
    assert str(0) __ solution.multiply("0", "0")
    assert str(123*456) __ solution.multiply("123", "456")
