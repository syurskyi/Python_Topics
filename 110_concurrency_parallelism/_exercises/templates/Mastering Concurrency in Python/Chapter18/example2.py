# ch18/example2.py

____ operator ______ mul
____ functools ______ reduce

___
    w__ T..:
        line _ in..('Please enter a list of integer, separated by commas: ')
        ___
            nums _ li..(m..(int, line.split(',')))
        ______ ValueError:
            print('ERROR. Enter only integers separated by commas')
            c..

        print('Sum of input integers', su.(nums))
        print('Product of input integers', reduce(mul, nums, 1))

______ K..
    print('\nFinished.')
