c_ Solution:
    # @return a list of strings, [s1, s2]
    ___ letterCombinations  d..):
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
        letter_combination_aux(0, d.., d, cand, res)
        r.. res

    ___ letter_combination_aux  i, d.., d, cand, res):
        __ i __ l..(d..):
            res.a..(''.j..(cand))
        ____:
            digit = d..[i]
            __ digit __ d:
                letters = d[digit]
                ___ letter __ letters:
                    cand.a..(letter)
                    letter_combination_aux(i + 1, d.., d, cand, res)
                    cand.pop()
