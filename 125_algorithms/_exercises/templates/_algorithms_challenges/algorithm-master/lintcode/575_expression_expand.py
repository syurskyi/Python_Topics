class Solution:
    ___ expressionExpand(self, s):
        """
        :type s: str
        :rtype: str
        """
        __ not s:
            return ''

        times = 0
        stack = []

        for c in s:
            __ c.isdigit():
                times = times * 10 + int(c)
            elif c == '[':
                stack.append(times)
                times = 0
            elif c == ']':
                part = []
                while stack and isinstance(stack[-1], str):
                    part.append(stack.pop())
                cnt = int(stack.pop()) __ stack else 1
                stack.append(cnt * ''.join(reversed(part)))
            else:
                stack.append(c)

        return ''.join(stack)
