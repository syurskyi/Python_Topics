"""
http://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python


In this kata you have to create all permutations of an input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

"""


___ permutations(string):
    result = set([string])
    __ l..(string) __ 2:
        result.add(string[1] + string[0])

    ____ l..(string) > 2:
        ___ i, c __ enumerate(string):
            ___ s __ permutations(string[:i] + string[i + 1:]):
                result.add(c + s)

    r.. l..(result)