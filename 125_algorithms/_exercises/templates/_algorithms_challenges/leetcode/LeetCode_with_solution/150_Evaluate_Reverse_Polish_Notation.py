c_ Solution o..
    ___ evalRPN  tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ___ t __ tokens:
            try:
                temp = int(t)
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
                    a = int(a * 1.0 / b)
                stack.append(a)
        r_ stack[-1]