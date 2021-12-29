'''
Created on Sep 6, 2017

@author: MT
'''
class Solution(object):
    ___ findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        ___ path __ paths:
            arr = path.s..(' ')
            folder = arr[0]
            files = arr[1:]
            ___ file __ files:
                arr0 = file.s..('(')
                content = arr0[1][:-1]
                filename = arr0[0]
                fullPath = folder+'/'+filename
                hashmap[content] = hashmap.get(content, []) + [fullPath]
        res    # list
        ___ _, value __ hashmap.items():
            __ l..(value) > 1:
                res.a..(value)
        r.. res
    
    ___ test(self):
        testCases = [
            ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
        ]
        ___ paths __ testCases:
            print('paths: %s' % paths)
            result = self.findDuplicate(paths)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
