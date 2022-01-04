'''
Created on Sep 13, 2017

@author: MT
'''
c_ Excel(object):

    ___ - , H, W):
        """
        :type H: int
        :type W: str
        """
        m = H
        n = ord(W)-ord('A')+1
        matrix = [[0]*n ___ _ __ r..(m)]
        hashmap    # dict

    ___ set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        i = r-1
        j = ord(c)-ord('A')
        diff = v-matrix[i][j]
        matrix[i][j] = v
        ___ (i0, j0), vals __ hashmap.i..:
            matrix[i0][j0] += diff*(vals.count((i, j)))
        __ (i, j) __ hashmap:
            del hashmap[(i, j)]

    ___ get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        i, j = r-1, ord(c)-ord('A')
        r.. matrix[i][j]

    ___ s..(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        i, j = r-1, ord(c)-ord('A')
        ___ (i0, j0), vals __ hashmap.i..:
            __ i0 __ i a.. j0 __ j:
                del hashmap[(i, j)]
                break
            ___ i1, j1 __ vals:
                __ i1 __ i a.. j1 __ j a.. (i, j) __ hashmap:
                    del hashmap[(i, j)]
                    break
        vals    # list
        sumVal = 0
        ___ s __ strs:
            arr = s.s..(':')
            __ l..(arr) __ 1:
                x = i..(arr[0][1:])-1
                y = ord(arr[0][0])-ord('A')
                vals.a..((x, y))
                sumVal += matrix[x][y]
            ____:
                x0 = i..(arr[0][1:])-1
                y0 = ord(arr[0][0])-ord('A')
                x1 = i..(arr[1][1:])-1
                y1 = ord(arr[1][0])-ord('A')
                ___ i0 __ r..(x0, x1+1):
                    ___ j0 __ r..(y0, y1+1):
                        vals.a..((i0, j0))
                        sumVal += matrix[i0][j0]
        hashmap[(i, j)] = vals
        matrix[i][j] = sumVal
        r.. sumVal

__ __name__ __ '__main__':
    excel = Excel(3, 'C')
    excel.set(1, 'A', 2)
    print(excel.s..(3, 'C', ['A1', 'A1:B2']))
    excel.set(2, 'B', 2)
    print(excel.get(3, 'C'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.get(1, 'A'))
    print(excel.set(1, 'A', 1))
    print(excel.get(1, 'A'))
    print(excel.s..(2, 'B', ['A1', 'A1']))
    print(excel.set(1, 'A', 2))
    print(excel.get(2, 'B'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.set(1, 'A', 1))
    print(excel.s..(2, 'B', ['A1']))
    print(excel.set(2, 'B', 0))
    print(excel.get(1, 'B'))
    print(excel.set(1, 'A', 5))
    print(excel.get(2, 'B'))
    print('-='*10+'-')

    excel = Excel(3, 'C')
    print(excel.s..(1, 'A', ['A2']))
    print(excel.set(2, 'A', 1))
    print(excel.get(1, 'A'))
    print('-='*10+'-')
