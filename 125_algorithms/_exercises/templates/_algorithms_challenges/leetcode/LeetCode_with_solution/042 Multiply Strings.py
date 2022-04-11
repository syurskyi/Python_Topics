"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
__author__ 'Danyang'


c_ Solution(o..
    ___ multiply  num1, num2
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
        __ l..(num1) > l..(num2  # order them first
            r.. multiply(num2, num1)

        # reverse them first
        num1 map(i.., l..(num1[::-1]
        num2 map(i.., l..(num2[::-1]

        # multiply by 1 digit at a time
        ___ d __ num1:
            result.a..(multiply_1_digit(d, num2

        # add the temporary results up
        lst add_list(result)

        # post processing
        lst.r..  # reverse back
        result "".j.. m..(s.., lst.l..("0")
        __ n.. result:
            r.. "0"
        r.. result

    ___ multiply_1_digit  digit, num
        """
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        """
        ret    # list

        carry 0
        ___ elt __ num:
            mul elt*digit + carry
            carry mul/10
            mul %= 10
            ret.a..(mul)

        __ carry != 0:
            ret.a..(carry)

        r.. ret

    ___ add_list  lst
        """
        add lst of string
        :param lst:
        :return:
        """
        sig 0
        ret [0]
        ___ ind, val __ e..(lst
            ___ i __ x..(sig val.insert(0, 0)  # possible deque
            ret add(ret, val)
            sig += 1
        r.. ret

    ___ add  num1, num2
        """
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        """

        __ l..(num1) > l..(num2
            r.. add(num2, num1)

        ret    # list
        carry 0
        ___ idx __ x..(l..(num2:  # longer one
            ___
                sm num1[idx] + num2[idx] + carry
            ______ I..
                sm num2[idx] + carry

            carry sm/10
            ret.a..(sm % 10)

        __ carry != 0:
            ret.a..(carry)

        r.. ret


__ _______ __ _______
    solution Solution()
    ... [1, 2] __ solution.add([2, 1], [9])
    ... s..(123*999) __ solution.multiply("123", "999")
    ... s..(0) __ solution.multiply("0", "0")
    ... s..(123*456) __ solution.multiply("123", "456")
