c_ Solution:
    # @return a list of strings, [s1, s2]
    ___ letterCombinations  d..
        d {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        r.. c..d.., 0, d)

    ___ combinations  d.., i, d
        __ i __ l..(d..
            r.. ['']
        ____
            res    # list
            rest_combs c..d.., i + 1, d)
            ___ comb __ rest_combs:
                number d..[i]
                letters d[number]
                ___ letter __ letters:
                    res.a..(letter + comb)
            r.. res
