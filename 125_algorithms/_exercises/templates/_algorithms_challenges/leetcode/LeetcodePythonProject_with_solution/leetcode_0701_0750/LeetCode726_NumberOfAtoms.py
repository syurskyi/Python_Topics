'''
Created on Feb 21, 2018

@author: tongq
'''
_______ re
class Solution(object):
    ___ countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        hashmap = self.helper(formula)
        arr = s..([str(c)+str(count) __ count > 1 ____ str(c) ___ c, count __ hashmap.items()])
        res = ''.join(arr)
        r.. res
    
    ___ helper(self, s):
        hashmap = {}
        i = 0
        while i < l..(s):
            __ s[i] __ '(':
                count0 = 1
                i += 1
                prev = i
                while i < l..(s) and count0 > 0:
                    __ s[i] __ ')':
                        count0 -= 1
                    ____ s[i] __ '(':
                        count0 += 1
                    i += 1
                hashmap0 = self.helper(s[prev:i-1])
                __ i __ l..(s) o. n.. s[i].isdigit():
                    count = 1
                ____:
                    prev = i
                    while i < l..(s) and s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                ___ elem, freq __ hashmap0.items():
                    hashmap[elem] = hashmap.get(elem, 0)+freq*count
            ____:
                __ i+1 < l..(s) and re.match('[a-z]', s[i+1]):
                    elem = s[i:i+2]
                    i+=1
                ____:
                    elem = s[i]
                i+=1
                __ i __ l..(s) o. n.. s[i].isdigit() o. s[i] __ '(':
                    count = 1
                ____:
                    prev = i
                    while i < l..(s) and s[i].isdigit():
                        i += 1
                    count = int(s[prev:i])
                hashmap[elem] = hashmap.get(elem, 0)+count
        r.. hashmap
    
    ___ test(self):
        testCases = [
#             'H2O',
#             'Mg(OH)2',
#             'K4(ON(SO3)2)2',
            '((N42)24(B11))2',
            '((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = self.countOfAtoms(s)
            print('result: %s' % result)
            print('-='*30+'-')
        
__ __name__ __ '__main__':
    Solution().test()
