'''
In this Bite you complete find_number_pairs which receives a list of numbers and returns all the pairs
that sum up N (default=10). Return this list of tuples from the function.

So in the most basic example if we pass in [2, 3, 5, 4, 6] it returns [(4, 6)] and if
we give it [9, 1, 3, 8, 7] it returns [(9, 1), (3, 7)]. The tests check more scenarios
(floats, other values of N, negative numbers).

Have fun and keep calm and code in Python
'''

___ find_number_pairs(numbers, N=10):

    result_possible_duplicates    # list
    ___ i __ numbers:
        number_to_find = N - i
        __ number_to_find __ l..(set(numbers) - set([i])):
            result_possible_duplicates.a..((i, number_to_find))
    result    # list
    # Reverse tuples so we can eliminate duplicates using set
    ___ p __ result_possible_duplicates:
        a,b = p
        temp = (a,b) __ a < b ____ (b,a)
        result.a..(temp)
    r.. l..(set(result))

print(find_number_pairs([0.24, 0.36, 0.04, 0.06, 0.33, 0.08, 0.20, 0.27, 0.3, 0.31,
          0.76, 0.05, 0.08, 0.08, 0.67, 0.09, 0.66, 0.79, 0.95], 1))
