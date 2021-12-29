'''
Created on Sep 16, 2019

@author: tongq
'''
class Solution(object):
    ___ buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ len(a) != len(b): return False
        __ a == b and len(set(a)) < len(a): return True
        dif = [(c1, c2) for c1, c2 in zip(a, b) __ c1 != c2]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
    
    ___ buddyStrings_own(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = A, B
        __ len(a) != len(b):
            return False
        c01, c02 = '', ''
        times = 0
        for c1, c2 in zip(a, b):
            __ c1 != c2:
                __ times > 1:
                    return False
                elif times == 1:
                    __ c01 == c2 and c02 == c1:
                        times += 1
                    else:
                        return False
                else:
                    c01, c02 = c1, c2
                    times += 1
        __ times == 0:
            return len(set(a)) < len(a)
        return times == 2
    
    ___ test(self):
        testCase = [
            ['ab', 'ba'],
            ['ab', 'ab'],
            ['aa', 'aa'],
            ['aaaaaabc', 'aaaaaacb'],
            ['', 'aa'],
        ]
        for a, b in testCase:
            res = self.buddyStrings(a, b)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
