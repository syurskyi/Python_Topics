___ last_digit(n1, n2
    res {
            1 : [1],
            2 : [2,4,8,6],
            3 : [3,9,7,1],
            4 : [4,6],
            5 : [5],
            6 : [6],
            7 : [7,9,3,1],
            8 : [8,4,2,6],
            9 : [9,1],
            0 : [0]
    }
    n1 %= 10
    __ n2 __ 0:
        r.. 1
    ____ n1 __ (1,5,6,0
        r.. n1
    ____
        r.. res[n1][n2%l..(res[n1]) - 1]

___ i __ r..(0,5
    print(last_digit(34,i