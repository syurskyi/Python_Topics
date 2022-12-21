'''
Created on Sep 13, 2017

@author: MT
'''
c_ Excel(o..

    ___ - , H, W
        """
        :type H: int
        :type W: str
        """
        m H
        n o..(W)-o..('A')+1
        matrix [[0]*n ___ _ __ r..(m)]
        hashmap    # dict

    ___ s..  r, c, v
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """
        i r-1
        j o..(c)-o..('A')
        diff v-matrix[i][j]
        matrix[i][j] v
        ___ (i0, j0), vals __ hashmap.i..
            matrix[i0][j0] += diff*(vals.c..((i, j)))
        __ (i, j) __ hashmap:
            del hashmap[(i, j)]

    ___ get  r, c
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        i, j r-1, o..(c)-o..('A')
        r.. matrix[i][j]

    ___ s..  r, c, strs
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        i, j r-1, o..(c)-o..('A')
        ___ (i0, j0), vals __ hashmap.i..
            __ i0 __ i a.. j0 __ j:
                del hashmap[(i, j)]
                _____
            ___ i1, j1 __ vals:
                __ i1 __ i a.. j1 __ j a.. (i, j) __ hashmap:
                    del hashmap[(i, j)]
                    _____
        vals    # list
        sumVal 0
        ___ s __ strs:
            arr s.s..(':')
            __ l..(arr) __ 1:
                x i..(arr[0][1:])-1
                y o..(arr 0 0 )-o..('A')
                vals.a..((x, y
                sumVal += matrix[x][y]
            ____
                x0 i..(arr[0][1:])-1
                y0 o..(arr 0 0 )-o..('A')
                x1 i..(arr[1][1:])-1
                y1 o..(arr[1] 0-o..('A')
                ___ i0 __ r..(x0, x1+1
                    ___ j0 __ r..(y0, y1+1
                        vals.a..((i0, j0
                        sumVal += matrix[i0][j0]
        hashmap[(i, j)] vals
        matrix[i][j] sumVal
        r.. sumVal

__ _____ __ _____
    excel Excel(3, 'C')
    excel.s..(1, 'A', 2)
    print(excel.s..(3, 'C',  'A1', 'A1:B2'
    excel.s..(2, 'B', 2)
    print(excel.g.. 3, 'C'
    print('-='*10+'-')
 
    excel Excel(5, 'E')
    print(excel.g.. 1, 'A'
    print(excel.s..(1, 'A', 1
    print(excel.g.. 1, 'A'
    print(excel.s..(2, 'B',  'A1', 'A1'
    print(excel.s..(1, 'A', 2
    print(excel.g.. 2, 'B'
    print('-='*10+'-')
 
    excel Excel(5, 'E')
    print(excel.s..(1, 'A', 1
    print(excel.s..(2, 'B',  'A1'
    print(excel.s..(2, 'B', 0
    print(excel.g.. 1, 'B'
    print(excel.s..(1, 'A', 5
    print(excel.g.. 2, 'B'
    print('-='*10+'-')

    excel Excel(3, 'C')
    print(excel.s..(1, 'A',  'A2'
    print(excel.s..(2, 'A', 1
    print(excel.g.. 1, 'A'
    print('-='*10+'-')
