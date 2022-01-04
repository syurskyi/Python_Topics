'''
Created on Feb 21, 2018

@author: tongq
'''
_______ __
c_ Solution(object):
    ___ countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        hashmap = helper(formula)
        arr = s..([s..(c)+s..(count) __ count > 1 ____ s..(c) ___ c, count __ hashmap.i..])
        res = ''.j..(arr)
        r.. res
    
    ___ helper(self, s):
        hashmap    # dict
        i = 0
        w.... i < l..(s):
            __ s[i] __ '(':
                count0 = 1
                i += 1
                prev = i
                w.... i < l..(s) a.. count0 > 0:
                    __ s[i] __ ')':
                        count0 -= 1
                    ____ s[i] __ '(':
                        count0 += 1
                    i += 1
                hashmap0 = helper(s[prev:i-1])
                __ i __ l..(s) o. n.. s[i].isdigit():
                    count = 1
                ____:
                    prev = i
                    w.... i < l..(s) a.. s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                ___ elem, freq __ hashmap0.i..:
                    hashmap[elem] = hashmap.get(elem, 0)+freq*count
            ____:
                __ i+1 < l..(s) a.. __.m..('[a-z]', s[i+1]):
                    elem = s[i:i+2]
                    i+=1
                ____:
                    elem = s[i]
                i+=1
                __ i __ l..(s) o. n.. s[i].isdigit() o. s[i] __ '(':
                    count = 1
                ____:
                    prev = i
                    w.... i < l..(s) a.. s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                hashmap[elem] = hashmap.get(elem, 0)+count
        r.. hashmap
    
    ___ test
        testCases = [
#             'H2O',
#             'Mg(OH)2',
#             'K4(ON(SO3)2)2',
            '((N42)24(B11))2',
            '((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = countOfAtoms(s)
            print('result: %s' % result)
            print('-='*30+'-')
        
__ __name__ __ '__main__':
    Solution().test()
