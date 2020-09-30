'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object
    ___ lengthLongestPath(self, input
        maxLen = 0
        pathLen = {0:0}
        ___ line __ input.splitlines(
            name = line.lstrip('\t')
            depth = le.(line)-le.(name)
            __ '.' __ name:
                maxLen = ma.(maxLen, pathLen[depth]+le.(name))
            ____
                pathLen[depth+1] = pathLen[depth]+le.(name)+1
        r_ maxLen
    
    ___ test(self
        testCases = [
#             'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tsubdir23\n\t\tsubsubdir23\n\t\t\tfile23.ext',
        ]
        ___ input __ testCases:
            print('input:\n%s' % input)
            result = self.lengthLongestPath(input)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
