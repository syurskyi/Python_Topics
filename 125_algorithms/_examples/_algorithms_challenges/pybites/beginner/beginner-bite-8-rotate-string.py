"""
Write a function that rotates characters in a string, in both directions:

if n is positive move characters from beginning to end, e.g.: rotate('hello', 2) would return llohe
if n is negative move characters to the start of the string, e.g.: rotate('hello', -2) would return lohel
See tests for more info. Have fun!

def test_rotate():
    assert rotate('hello', 2) == 'llohe'
    assert rotate('hello', -2) == 'lohel'

    string = 'bob and julian love pybites!'
    expected = 'love pybites!bob and julian '
    assert rotate(string, 15) == expected

    string = 'pybites loves julian and bob!'
    expected = 'julian and bob!pybites loves '
    assert rotate(string, -15) == expected

"""
import collections

def rotate(string, n):
    """Rotate characters in a string. Expects string and n (int) for
       number of characters to move.
    """
    d = collections.deque(string)
    d.rotate(-n)
    result = ''.join(d)
    print(result)



rotate('bob and julian love pybites!', 15)
