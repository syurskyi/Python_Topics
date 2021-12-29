__author__ = 'Danyang'


class Solution(object):
    ___ evalRPN(self, tokens):
        """
        stack
        basic in bytecode operation
        basic in compiler technique
        :param tokens:
        :return:
        """
        ops = ["+", "-", "*", "/"]

        ___ arith(a, b, op):
            __ (op == "+"):
                return a+b
            __ (op == "-"):
                return a-b
            __ (op == "/"):
                # return a/b # python treat differently for division 6/-132 is -1
                return int(float(a)/b)  # round towards 0
            __ (op == "*"):
                return a*b

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
        stack = []
        for token in tokens:
            __ token not in ops:
                stack.append(int(token))
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arith(arg1, arg2, token)
                stack.append(result)
        return stack.pop()


__ __name__ == "__main__":
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22