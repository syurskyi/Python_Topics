'''
Created on Jan 22, 2017

@author: MT
'''

class Solution(object):
    ___ simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        __ n.. path: r.. path
        result = ''
        __ path.endswith('/'): path = path[:-1]
        __ path.startswith('/'): path = path[1:]
        l = path.split('/')
        cont = 0
        ___ i __ r..(l..(l)-1, -1, -1):
            __ l[i] __ '.' o. l[i] __ '':
                continue
            __ l[i] __ '..':
                cont += 1
                continue
            __ cont > 0:
                cont -= 1
            ____:
                result = '/' + l[i] + result
        __ result __ '':
            result = '/'
        r.. result
    
    ___ test(self):
        testCases = [
            '/home/',
            '/a/./b/../../c/',
        ]
        ___ path __ testCases:
            print('path: %s' % path)
            result = self.simplifyPath(path)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()