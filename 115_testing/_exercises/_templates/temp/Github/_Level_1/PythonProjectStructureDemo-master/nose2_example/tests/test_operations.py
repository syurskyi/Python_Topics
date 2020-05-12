____ u__ ______ T..
____ my_package ______ MyApp

c_ TestOperations(T..
    ___ setUp
        app _ MyApp()
    ___ test_add
        aE..(app.do('add', 3, 4), 7)
        aE..(app.do('ADD', 3, 4), 7)
    ___ test_multiply
        aE..(app.do('multiply', 3, 4), 12)
    ___ test_substract
        aE..(app.do('substract', 3, 4), -1)
