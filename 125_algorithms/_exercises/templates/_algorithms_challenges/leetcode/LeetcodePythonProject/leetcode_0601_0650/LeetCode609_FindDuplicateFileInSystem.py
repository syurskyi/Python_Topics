'''
Created on Sep 6, 2017

@author: MT
'''
class Solution(object
    ___ findDuplicate(self, paths
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        ___ path in paths:
            arr = path.split(' ')
            folder = arr[0]
            files = arr[1:]
            ___ file in files:
                arr0 = file.split('(')
                content = arr0[1][:-1]
                filename = arr0[0]
                fullPath = folder+'/'+filename
                hashmap[content] = hashmap.get(content, []) + [fullPath]
        res = []
        ___ _, value in hashmap.items(
            __ le.(value) > 1:
                res.append(value)
        r_ res
    
    ___ test(self
        testCases = [
            ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"],
        ]
        ___ paths in testCases:
            print('paths: %s' % paths)
            result = self.findDuplicate(paths)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
