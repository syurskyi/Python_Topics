c_ Solution:
    # @return a list of strings, [s1, s2]
    ___ letterCombinations  d..
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        cand    # list
        res    # list
        letter_combination_aux(d.., d, cand, res)
        r.. res

    ___ letter_combination_aux  d.., d, cand, res
        __ n.. d..:
            res.a..(''.j..(cand
        ____:
            digit = d..[0]
            __ digit __ d:
                letters = d[digit]
                ___ letter __ letters:
                    cand.a..(letter)
                    letter_combination_aux(d..[1:], d, cand, res)
                    cand.pop()
