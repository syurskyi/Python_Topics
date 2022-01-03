'''
Created on Mar 11, 2017

@author: MT
'''

c_ Solution(object):
    ___ minArea(self, image, x, y):
        m, n = l..(image), l..(image[0])
        left = searchColumns(image, 0, y, 0, m, T..)
        right = searchColumns(image, y+1, n, 0, m, F..)
        top = searchRows(image, 0, x, left, right, T..)
        bottom = searchRows(image, x+1, m, left, right, F..)
        r.. (right-left)*(bottom-top)
    
    ___ searchColumns(self, image, i, j, top, bottom, opt):
        w.... i < j:
            k, mid = top, (i+j)//2
            w.... k < bottom a.. image[k][mid] __ '0':
                k+=1
            __ (k < bottom) __ opt:
                j = mid
            ____:
                i = mid+1
        r.. i
    
    ___ searchRows(self, image, i, j, left, right, opt):
        w.... i < j:
            k, mid = left, (i+j)//2
            w.... k < right a.. image[mid][k] __ '0':
                k+=1
            __ (k < right) __ opt:
                j = mid
            ____:
                i  = mid+1
        r.. i
    
    ___ test
        testCases = [
            (
                [
                    '0010',
                    '0110',
                    '0100',
                ],
                0, 2
            ),
        ]
        ___ image, x, y __ testCases:
            result = minArea(image, x, y)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
