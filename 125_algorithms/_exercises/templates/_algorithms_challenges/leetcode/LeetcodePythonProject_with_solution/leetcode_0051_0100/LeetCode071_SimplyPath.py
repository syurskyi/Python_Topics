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
        __ not path: return path
        result = ''
        __ path.endswith('/'): path = path[:-1]
        __ path.startswith('/'): path = path[1:]
        l = path.split('/')
        cont = 0
        for i in range(len(l)-1, -1, -1):
            __ l[i] == '.' or l[i] == '':
                continue
            __ l[i] == '..':
                cont += 1
                continue
            __ cont > 0:
                cont -= 1
            else:
                result = '/' + l[i] + result
        __ result == '':
            result = '/'
        return result
    
    ___ test(self):
        testCases = [
            '/home/',
            '/a/./b/../../c/',
        ]
        for path in testCases:
            print('path: %s' % path)
            result = self.simplifyPath(path)
            print('result: %s' % result)
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()