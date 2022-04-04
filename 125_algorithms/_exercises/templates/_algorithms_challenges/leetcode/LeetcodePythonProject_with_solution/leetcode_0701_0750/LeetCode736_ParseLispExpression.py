'''
Created on Mar 10, 2018

@author: tongq
'''
c_ Solution(o..
    ___ evaluate  expression
        """
        :type expression: str
        :rtype: int
        """
        st, d, tokens    # list, {}, ['']
        
        ___ getVal(x
            r.. d.g.. x, x)
        
        ___ evaluate(tokens
            __ tokens[0] __ ('add', 'mult'
                tmp = l.. m..(i.., map(getVal, tokens[1:])))
                r.. s..(tmp[0]+tmp[1] __ tokens[0]__'add' ____ tmp[0]*tmp[1])
            ____
                ___ i __ r..(1, l..(tokens)-1, 2
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
                tokens, d = st.p.. )
                tokens[-1] += val
            ____
                tokens[-1] += c
        r.. i..(tokens[0])
    
    ___ evaluate_own_error  expression
        """
        :type expression: str
        :rtype: int
        """
        hashmap    # dict
        r.. helper(expression, hashmap)
    
    ___ helper  exp, hashmap
        __ exp[0] __ '-' o. exp.i..
            r.. i..(exp)
        ____ exp[0] != '(':
            r.. hashmap[exp]
        ____
            exp = exp[1:-1]
            __ exp[:3] __ 'add':
                sub1, i = nextElem(exp, 4)
                sub2, _ = nextElem(exp, i+1)
                res = helper(sub1, hashmap)+helper(sub2, hashmap)
                r.. res
            ____ exp[:4] __ 'mult':
                sub1, i = nextElem(exp, 5)
                sub2, _ = nextElem(exp, i+1)
                res = helper(sub1, hashmap)*helper(sub2, hashmap)
                r.. res
            ____
                i = 3
                w... T...
                    sub1, i = nextElem(exp, i+1)
                    __ i __ l..(exp
                        r.. helper(sub1, hashmap)
                    sub2, i = nextElem(exp, i+1)
                    hashmap[sub1] = helper(sub2, hashmap)
    
    ___ nextElem  s, i
        res = ''
        __ i >= l..(s
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
        ____
            w.... i < l..(s) a.. s[i] != ' ':
                res += s[i]
                i += 1
            r.. res, i
    
    ___ test
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
            result = evaluate(expression)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
