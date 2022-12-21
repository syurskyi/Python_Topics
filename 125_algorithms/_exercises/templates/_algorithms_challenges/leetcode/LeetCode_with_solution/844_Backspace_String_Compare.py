c_ Solution o..
    ___ backspaceCompare  S, T
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        __ S __ T:
            r_ T..
        s_stack =    # list
        t_stack =    # list
        ___ c __ S:
            __ c != '#':
                s_stack.append(c)
            ____ l.. s_stack) != 0:
                s_stack.pop(-1)
        ___ c __ T:
            __ c != '#':
                t_stack.append(c)
            ____ l.. t_stack) != 0:
                t_stack.pop(-1)
        r_ ''.join(s_stack) __ ''.join(t_stack)

    # def backspaceCompare(self, S, T):
    #     # https://leetcode.com/problems/backspace-string-compare/discuss/135603/C%2B%2BJavaPython-O(N)-time-and-O(1)-space
    #     back = lambda res, c: res[:-1] if c == '#' else res + c
    #     return reduce(back, S, "") == reduce(back, T, "")

    # def backspaceCompare(self, S, T):
    #     def back(res, c):
    #         if c != '#': res.append(c)
    #         elif res: res.pop()
    #         return res
    #     return reduce(back, S, []) == reduce(back, T, [])


    # def backspaceCompare(self, S, T):
    #     i, j = len(S) - 1, len(T) - 1
    #     backS = backT = 0
    #     while True:
    #         while i >= 0 and (backS or S[i] == '#'):
    #             backS += 1 if S[i] == '#' else -1
    #             i -= 1
    #         while j >= 0 and (backT or T[j] == '#'):
    #             backT += 1 if T[j] == '#' else -1
    #             j -= 1
    #         if not (i >= 0 and j >= 0 and S[i] == T[j]):
    #             return i == j == -1
    #         i, j = i - 1, j - 1
