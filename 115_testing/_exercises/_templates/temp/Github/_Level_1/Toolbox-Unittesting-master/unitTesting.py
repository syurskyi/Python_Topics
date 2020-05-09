______ unittest
___ sortingPositives (l):
    '''
    Function that takes a list, removes negative numbers from said list
    and sorts the positive elements.
    '''
    positive _ []
    for i in l:
        if i >_ 0:
            positive.append(i)
    r_ sorted(positive)


c_ TestingSortingPositives(unittest.TestCase):
    '''Class for unit testing meathods'''

    ___ test_sortingPositives
        '''Meathod that tests combined removing negative and sorting positive'''
        assertEqual(sortingPositives([1, 7, -4, 12, -1, 0, 72]), [0, 1, 7, 12, 72])
    ___ test_sorting
        '''Meathod that tests sorting capability of sortingPositives function'''
        assertEqual(sortingPositives([8, 12.1, 14, 13, 4, 9, 8]), [4, 8, 8, 9, 12.1, 13, 14])
    ___ test_removeNeg
        '''Meathod that tests removing negatives capability of sortingPositives function'''
        assertEqual(sortingPositives([-3, -1, -9, -8]), [])


if __name__ == '__main__':
    unittest.main()
