'''
Created on Apr 2, 2017

@author: MT
'''

c_ Solution(object):
    ___ lengthLongestPath  input):
        maxLen = 0
        pathLen = {0:0}
        ___ line __ input.splitlines
            name = line.lstrip('\t')
            depth = l..(line)-l..(name)
            __ '.' __ name:
                maxLen = m..(maxLen, pathLen[depth]+l..(name))
            ____:
                pathLen[depth+1] = pathLen[depth]+l..(name)+1
        r.. maxLen
    
    ___ test
        testCases = [
#             'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tsubdir23\n\t\tsubsubdir23\n\t\t\tfile23.ext',
        ]
        ___ input __ testCases:
            print('input:\n%s' % input)
            result = lengthLongestPath(input)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
