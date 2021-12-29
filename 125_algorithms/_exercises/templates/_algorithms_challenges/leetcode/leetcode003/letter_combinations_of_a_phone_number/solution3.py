class Solution:
    # @return a list of strings, [s1, s2]
    ___ letterCombinations(self, digits):
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
        self.letter_combination_aux(0, digits, d, cand, res)
        r.. res

    ___ letter_combination_aux(self, i, digits, d, cand, res):
        __ i __ l..(digits):
            res.a..(''.join(cand))
        ____:
            digit = digits[i]
            __ digit __ d:
                letters = d[digit]
                ___ letter __ letters:
                    cand.a..(letter)
                    self.letter_combination_aux(i + 1, digits, d, cand, res)
                    cand.pop()
