______ u__
___ sortingPositives (l
    '''
    Function that takes a list, removes negative numbers from said list
    and sorts the positive elements.
    '''
    positive _ # list
    ___ i __ l:
        __ i >_ 0:
            positive.a..(i)
    r_ sorted(positive)


c_ TestingSortingPositives?.?
    '''Class for unit testing meathods'''

    ___ test_sortingPositives
        '''Meathod that tests combined removing negative and sorting positive'''
        aE..(sortingPositives([1, 7, -4, 12, -1, 0, 72]), [0, 1, 7, 12, 72])
    ___ test_sorting
        '''Meathod that tests sorting capability of sortingPositives function'''
        aE..(sortingPositives([8, 12.1, 14, 13, 4, 9, 8]), [4, 8, 8, 9, 12.1, 13, 14])
    ___ test_removeNeg
        '''Meathod that tests removing negatives capability of sortingPositives function'''
        aE..(sortingPositives([-3, -1, -9, -8]), [])


__ _____ __ _____
    ?.?
