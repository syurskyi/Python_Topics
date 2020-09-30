class Solution:
    ___ expressionExpand(self, s
        """
        :type s: str
        :rtype: str
        """
        __ not s:
            r_ ''

        times = 0
        stack =   # list

        ___ c __ s:
            __ c.isdigit(
                times = times * 10 + int(c)
            ____ c __ '[':
                stack.append(times)
                times = 0
            ____ c __ ']':
                part =   # list
                w___ stack and isinstance(stack[-1], str
                    part.append(stack.pop())
                cnt = int(stack.pop()) __ stack else 1
                stack.append(cnt * ''.join(reversed(part)))
            ____
                stack.append(c)

        r_ ''.join(stack)
