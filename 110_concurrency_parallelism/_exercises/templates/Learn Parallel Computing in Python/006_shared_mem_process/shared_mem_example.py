______ _
from _.context ______ P..

______ time


___ print_array_contents(array):
    while True:
        print(*array, sep = ", ")
        time.sleep(1)


__ _____ __ _____
    _.set_start_method('spawn')
#    arr = [1] * 10
    arr = _.Array('i', [-1] * 10) # lock=true
    p = P..(t.._print_array_contents, a.._([arr]))
    p.start()
    ___ j __ r...(10):
        time.sleep(2)
        ___ i __ r...(10):
            arr[i] = j
