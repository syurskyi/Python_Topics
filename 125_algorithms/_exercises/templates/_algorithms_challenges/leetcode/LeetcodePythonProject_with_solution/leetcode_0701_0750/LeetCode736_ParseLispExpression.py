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
        st, d, tokens = [], {}, ['']
        
        ___ getVal(x):
            return d.get(x, x)
        
        ___ evaluate(tokens):
            __ tokens[0] in ('add', 'mult'):
                tmp = list(map(int, map(getVal, tokens[1:])))
                return str(tmp[0]+tmp[1] __ tokens[0]=='add' else tmp[0]*tmp[1])
            else:
                for i in range(1, len(tokens)-1, 2):
                    __ tokens[i+1]:
                        d[tokens[i]] = getVal(tokens[i+1])
                return getVal(tokens[-1])
        
        for c in expression:
            __ c == '(':
                __ tokens[0] == 'let':
                    evaluate(tokens)
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ' ':
                tokens.append('')
            elif c == ')':
                val = evaluate(tokens)
                tokens, d = st.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c
        return int(tokens[0])
    
    ___ evaluate_own_error(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        hashmap = {}
        return self.helper(expression, hashmap)
    
    ___ helper(self, exp, hashmap):
        __ exp[0] == '-' or exp.isdigit():
            return int(exp)
        elif exp[0] != '(':
            return hashmap[exp]
        else:
            exp = exp[1:-1]
            __ exp[:3] == 'add':
                sub1, i = self.nextElem(exp, 4)
                sub2, _ = self.nextElem(exp, i+1)
                res = self.helper(sub1, hashmap)+self.helper(sub2, hashmap)
                return res
            elif exp[:4] == 'mult':
                sub1, i = self.nextElem(exp, 5)
                sub2, _ = self.nextElem(exp, i+1)
                res = self.helper(sub1, hashmap)*self.helper(sub2, hashmap)
                return res
            else:
                i = 3
                while True:
                    sub1, i = self.nextElem(exp, i+1)
                    __ i == len(exp):
                        return self.helper(sub1, hashmap)
                    sub2, i = self.nextElem(exp, i+1)
                    hashmap[sub1] = self.helper(sub2, hashmap)
    
    ___ nextElem(self, s, i):
        res = ''
        __ i >= len(s):
            return res, i
        elif s[i] == '(':
            res = '('
            count = 1
            i += 1
            while i < len(s) and count > 0:
                __ s[i] == '(':
                    count += 1
                elif s[i] == ')':
                    count -= 1
                res += s[i]
                i += 1
            return res, i
        else:
            while i < len(s) and s[i] != ' ':
                res += s[i]
                i += 1
            return res, i
    
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
        for expression in testCases:
            print('expression: %s' % expression)
            result = self.evaluate(expression)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
