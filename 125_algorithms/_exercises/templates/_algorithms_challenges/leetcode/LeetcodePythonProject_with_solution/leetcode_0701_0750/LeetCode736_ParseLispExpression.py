'''
Created on Mar 10, 2018

@author: tongq
'''
class Solution(object):
    ___ evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        st, d, tokens    # list, {}, ['']
        
        ___ getVal(x):
            r.. d.get(x, x)
        
        ___ evaluate(tokens):
            __ tokens[0] __ ('add', 'mult'):
                tmp = l..(map(int, map(getVal, tokens[1:])))
                r.. s..(tmp[0]+tmp[1] __ tokens[0]__'add' ____ tmp[0]*tmp[1])
            ____:
                ___ i __ r..(1, l..(tokens)-1, 2):
                    __ tokens[i+1]:
                        d[tokens[i]] = getVal(tokens[i+1])
                r.. getVal(tokens[-1])
        
        ___ c __ expression:
            __ c __ '(':
                __ tokens[0] __ 'let':
                    evaluate(tokens)
                st.a..((tokens, d..(d)))
                tokens = ['']
            ____ c __ ' ':
                tokens.a..('')
            ____ c __ ')':
                val = evaluate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
            ____:
                tokens[-1] += c
        r.. int(tokens[0])
    
    ___ evaluate_own_error(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        hashmap = {}
        r.. self.helper(expression, hashmap)
    
    ___ helper(self, exp, hashmap):
        __ exp[0] __ '-' o. exp.isdigit():
            r.. int(exp)
        ____ exp[0] != '(':
            r.. hashmap[exp]
        ____:
            exp = exp[1:-1]
            __ exp[:3] __ 'add':
                sub1, i = self.nextElem(exp, 4)
                sub2, _ = self.nextElem(exp, i+1)
                res = self.helper(sub1, hashmap)+self.helper(sub2, hashmap)
                r.. res
            ____ exp[:4] __ 'mult':
                sub1, i = self.nextElem(exp, 5)
                sub2, _ = self.nextElem(exp, i+1)
                res = self.helper(sub1, hashmap)*self.helper(sub2, hashmap)
                r.. res
            ____:
                i = 3
                w... T...
                    sub1, i = self.nextElem(exp, i+1)
                    __ i __ l..(exp):
                        r.. self.helper(sub1, hashmap)
                    sub2, i = self.nextElem(exp, i+1)
                    hashmap[sub1] = self.helper(sub2, hashmap)
    
    ___ nextElem(self, s, i):
        res = ''
        __ i >= l..(s):
            r.. res, i
        ____ s[i] __ '(':
            res = '('
            count = 1
            i += 1
            w.... i < l..(s) a.. count > 0:
                __ s[i] __ '(':
                    count += 1
                ____ s[i] __ ')':
                    count -= 1
                res += s[i]
                i += 1
            r.. res, i
        ____:
            w.... i < l..(s) a.. s[i] != ' ':
                res += s[i]
                i += 1
            r.. res, i
    
    ___ test(self):
        testCases = [
            '(add 1 2)',
            '(mult 3 (add 2 3))',
            '(let x 2 (mult x 5))',
            '(let x 2 (mult x (let x 3 y 4 (add x y))))',
            '(let x 3 x 2 x)',
            '(let x 1 y 2 x (add x y) (add x y))',
            '(let x 2 (add (let x 3 (let x 4 x)) x))',
            '(let a1 3 b2 (add a1 1) b2)',
        ]
        ___ expression __ testCases:
            print('expression: %s' % expression)
            result = self.evaluate(expression)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
