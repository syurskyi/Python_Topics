# class Solution(object):
#     def isValid(self, s):
        
#
c_ Solution:
    ___ isValid  s
        """
        :type s: str
        :rtype: bool
        """
        __ s is N..:
            r_ T..
        stack =    # list
        ___ t __ s:
            __ t __ ')':
                try:
                    current = stack.pop()
                    __ current != '(':
                        r_ F..
                except:
                    r_ F..
            ____ t __ '}':
                try:
                    current = stack.pop()
                    __ current != '{':
                        r_ F..
                except:
                    r_ F..
            ____ t __ ']':
                try:
                    current = stack.pop()
                    __ current != '[':
                        r_ F..
                except:
                    r_ F..
            ____
                stack.append(t)
        __ l.. stack) __ 0:
            r_ T..
        ____
            r_ F..


    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False
