# class Solution(object):
#     def isValid(self, s):
        
#
c_ Solution:
    ___ isValid  s):
        """
        :type s: str
        :rtype: bool
        """
        __ s is N..:
            r_ True
        stack = []
        ___ t __ s:
            __ t __ ')':
                try:
                    current = stack.pop()
                    __ current != '(':
                        r_ False
                except:
                    r_ False
            ____ t __ '}':
                try:
                    current = stack.pop()
                    __ current != '{':
                        r_ False
                except:
                    r_ False
            ____ t __ ']':
                try:
                    current = stack.pop()
                    __ current != '[':
                        r_ False
                except:
                    r_ False
            ____
                stack.append(t)
        __ l.. stack) __ 0:
            r_ True
        ____
            r_ False


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
