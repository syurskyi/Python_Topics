'''
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others.
He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one
(the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details
'''

_______ s__
____ e.. _______ E..


c_ State(E..
    ALPHANUMERIC 1
    NON_ALPHANUMERIC 2

___ get_index_different_char(chars
    index 1
    __ chars[0] __ s__.ascii_letters o. s__.d..:
        state State.ALPHANUMERIC
    ____
        state State.NON_ALPHANUMERIC
    ___ c __ chars[1:]:
        __ c __ (s__.ascii_letters o. s__.d..) a.. state __ State.ALPHANUMERIC:
            _____
        __ c __ (s__.ascii_letters o. s__.d..) a.. state __ State.NON_ALPHANUMERIC:


