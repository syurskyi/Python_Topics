"""
http://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python


In this kata you have to create all permutations of an input string and remove duplicates, if present.
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

"""


___ p..(s__
    result = s..([s__])
    __ l..(s__) __ 2:
        result.add(s__[1] + s__[0])

    ____ l..(s__) > 2:
        ___ i, c __ e..(s__
            ___ s __ permutations(s__[:i] + s__[i + 1:]
                result.add(c + s)

    r.. l..(result)