c_ Solution:
    ___ expressionExpand(self, s):
        """
        :type s: str
        :rtype: str
        """
        __ n.. s:
            r.. ''

        times = 0
        stack    # list

        ___ c __ s:
            __ c.isdigit
                times = times * 10 + i..(c)
            ____ c __ '[':
                stack.a..(times)
                times = 0
            ____ c __ ']':
                part    # list
                w.... stack a.. isi..(stack[-1], s..):
                    part.a..(stack.pop())
                cnt = i..(stack.pop()) __ stack ____ 1
                stack.a..(cnt * ''.j..(r..(part)))
            ____:
                stack.a..(c)

        r.. ''.j..(stack)
