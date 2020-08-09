class Solution:
    # @return a list of strings, [s1, s2]
    ___ letterCombinations(self, digits
        d = {
            '2': 'abc',
            '3': '___',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        r_ self.combinations(digits, 0, d)

    ___ combinations(self, digits, i, d
        __ i __ le.(digits
            r_ ['']
        ____
            res = []
            rest_combs = self.combinations(digits, i + 1, d)
            for comb in rest_combs:
                number = digits[i]
                letters = d[number]
                for letter in letters:
                    res.append(letter + comb)
            r_ res
