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
        self.letter_combination_aux(digits, d, cand, res)
        r.. res

    ___ letter_combination_aux(self, digits, d, cand, res):
        __ n.. digits:
            res.a..(''.join(cand))
        ____:
            digit = digits[0]
            __ digit __ d:
                letters = d[digit]
                ___ letter __ letters:
                    cand.a..(letter)
                    self.letter_combination_aux(digits[1:], d, cand, res)
                    cand.pop()
