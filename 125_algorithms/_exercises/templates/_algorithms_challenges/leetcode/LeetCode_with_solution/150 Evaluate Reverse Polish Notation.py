__author__ = 'Danyang'


c_ Solution(o..):
    ___ evalRPN  tokens):
        """
        stack
        basic in bytecode operation
        basic in compiler technique
        :param tokens:
        :return:
        """
        ops = ["+", "-", "*", "/"]

        ___ arith(a, b, op):
            __ (op __ "+"):
                r.. a+b
            __ (op __ "-"):
                r.. a-b
            __ (op __ "/"):
                # return a/b # python treat differently for division 6/-132 is -1
                r.. i..(float(a)/b)  # round towards 0
            __ (op __ "*"):
                r.. a*b

        # function is first-order class
        # not supported by leetcode
        # import operator
        # ops = {
        # "+": operator.add,
        #     "-": operator.sub,
        #     "*": operator.mul,
        #     "/": operator.div,
        # }
        #
        # def arith(a, b, op):
        #     return ops[op](a, b)

        # stack
        stack    # list
        ___ token __ tokens:
            __ token n.. __ ops:
                stack.a..(i..(token))
            ____:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arith(arg1, arg2, token)
                stack.a..(result)
        r.. stack.pop()


__ _______ __ _______
    ... Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) __ 22