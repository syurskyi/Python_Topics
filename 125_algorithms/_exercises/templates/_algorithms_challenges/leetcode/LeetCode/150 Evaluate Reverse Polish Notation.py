__author__ = 'Danyang'


class Solution(object
    ___ evalRPN(self, tokens
        """
        stack
        basic in bytecode operation
        basic in compiler technique
        :param tokens:
        :return:
        """
        ops = ["+", "-", "*", "/"]

        ___ arith(a, b, op
            __ (op __ "+"
                r_ a+b
            __ (op __ "-"
                r_ a-b
            __ (op __ "/"
                # return a/b # python treat differently for division 6/-132 is -1
                r_ int(float(a)/b)  # round towards 0
            __ (op __ "*"
                r_ a*b

        # function is first-order class
        # not supported by leetcode
        # ______ operator
        # ops = {
        # "+": operator.add,
        #     "-": operator.sub,
        #     "*": operator.mul,
        #     "/": operator.div,
        # }
        #
        # ___ arith(a, b, op
        #     return ops[op](a, b)

        # stack
        stack = []
        for token in tokens:
            __ token not in ops:
                stack.append(int(token))
            ____
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arith(arg1, arg2, token)
                stack.append(result)
        r_ stack.pop()


__ __name__ __ "__main__":
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) __ 22