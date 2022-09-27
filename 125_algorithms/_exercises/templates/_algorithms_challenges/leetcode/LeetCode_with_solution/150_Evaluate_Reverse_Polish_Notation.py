c_ Solution o..
    ___ evalRPN  tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack =    # list
        ___ t __ tokens:
            try:
                temp = i..(t)
                stack.append(temp)
            except:
                b = stack.pop()
                a = stack.pop()
                __ t __ "+":
                    a += b
                ____ t __ "-":
                    a -= b
                ____ t __ "*":
                    a *= b
                ____
                    a = i..(a * 1.0 / b)
                stack.append(a)
        r_ stack[-1]