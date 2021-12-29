'''
Created on Nov 6, 2017

@author: MT
'''
class Solution(object):
    ___ isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            __ c in ['(', '{', '[']:
                stack.append(c)
            else:
                __  (c == ')' and stack and stack[-1]=='(') or\
                    (c == ']' and stack and stack[-1]=='[') or\
                    (c == '}' and stack and stack[-1]=='{'):
                    stack.pop()
                else:
                    return False
        return stack == []
    
    ___ test(self):
        testCases = [
            '(){}[]',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.isValid(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
